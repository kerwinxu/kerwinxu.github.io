---
title: "C# Winform 跨线程更新UI控件常用方法汇总"
date: "2019-04-23"
categories: 
  - "c"
---

C#Winform编程中，跨线程直接更新UI控件的做法是不正确的，会时常出现“线程间操作无效: 从不是创建控件的线程访问它”的异常。处理跨线程更新Winform UI控件常用的方法有4种：

# 通过UI线程的SynchronizationContext的Post/Send方法更新

```
//共分三步
       //第一步：获取UI线程同步上下文（在窗体构造函数或FormLoad事件中）
       /// <summary>
       /// UI线程的同步上下文
       /// </summary>
       SynchronizationContext m_SyncContext = null;
       public Form1()
       {
           InitializeComponent();
           //获取UI线程同步上下文
           m_SyncContext = SynchronizationContext.Current;
           //Control.CheckForIllegalCrossThreadCalls = false;
       }
       //第二步：定义线程的主体方法
       /// <summary>
       /// 线程的主体方法
       /// </summary>
       private void ThreadProcSafePost()
       {
           //...执行线程任务

           //在线程中更新UI（通过UI线程同步上下文m_SyncContext）
           m_SyncContext.Post(SetTextSafePost, "This text was set safely by SynchronizationContext-Post.");

           //...执行线程其他任务
       }
       //第三步：定义更新UI控件的方法
       /// <summary>
       /// 更新文本框内容的方法
       /// </summary>
       /// <param name="text"></param>
       private void SetTextSafePost(object text)
       {
           this.textBox1.Text = text.ToString();
       }
       //之后,启动线程
       /// <summary>
       /// 启动线程按钮事件
       /// </summary>
       /// <param name="sender"></param>
       /// <param name="e"></param>
       private void setSafePostBtn_Click(object sender, EventArgs e)
       {
           this.demoThread = new Thread(new ThreadStart(this.ThreadProcSafePost));
           this.demoThread.Start();
       }
```

 

该方法的主要原理是：在线程执行过程中，需要更新到UI控件上的数据不再直接更新，而是通过UI线程上下文的Post/Send方法，将数据以异步/同步消息的形式发送到UI线程的消息队列；UI线程收到该消息后，根据消息是异步消息还是同步消息来决定通过异步/同步的方式调用SetTextSafePost方法直接更新自己的控件了。

在本质上，向UI线程发送的消息并是不简单数据，而是一条委托调用命令。

//在线程中更新UI（通过UI线程同步上下文m\_SyncContext） m\_SyncContext.Post(SetTextSafePost, "This text was set safely by SynchronizationContext-Post."); 可以这样解读这行代码：向UI线程的同步上下文（m\_SyncContext）中提交一个异步消息(UI线程，你收到消息后以异步的方式执行委托,调用方法SetTextSafePost，参数是“this text was ....”).

# 通过UI控件的Invoke/BeginInvoke方法更新

```
// 共分三步

        // 第一步：定义委托类型
        // 将text更新的界面控件的委托类型
        delegate void SetTextCallback(string text);

        //第二步：定义线程的主体方法
        /// <summary>
        /// 线程的主体方法
        /// </summary>
        private void ThreadProcSafe()
        {
            //...执行线程任务

            //在线程中更新UI（通过控件的.Invoke方法）
            this.SetText("This text was set safely.");

            //...执行线程其他任务
        }
        //第三步：定义更新UI控件的方法
        /// <summary>
        /// 更新文本框内容的方法
        /// </summary>
        /// <param name="text"></param>
        private void SetText(string text)
        {
            // InvokeRequired required compares the thread ID of the 
            // calling thread to the thread ID of the creating thread. 
            // If these threads are different, it returns true. 
            if (this.textBox1.InvokeRequired)//如果调用控件的线程和创建创建控件的线程不是同一个则为True
            {
                while (!this.textBox1.IsHandleCreated)
                {
                    //解决窗体关闭时出现“访问已释放句柄“的异常
                    if (this.textBox1.Disposing || this.textBox1.IsDisposed)
                        return;
                }
                SetTextCallback d = new SetTextCallback(SetText);
                this.textBox1.Invoke(d, new object[] { text });
            }
            else
            {
                this.textBox1.Text = text;
            }
        }
        //之后,启动线程
        /// <summary>
        /// 启动线程按钮事件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void setTextSafeBtn_Click(
            object sender,
            EventArgs e)
        {
            this.demoThread =
                new Thread(new ThreadStart(this.ThreadProcSafe));

            this.demoThread.Start();
        }

```

 

说明：这个方法是目前跨线程更新UI使用的主流方法，使用控件的Invoke/BeginInvoke方法，将委托转到UI线程上调用，实现线程安全的更新。原理与方法1类似，本质上还是把线程中要提交的消息，通过控件句柄调用委托交到UI线程中去处理。

# 通过BackgroundWorker取代Thread执行异步操作

```
//共分三步

        //第一步：定义BackgroundWorker对象，并注册事件（执行线程主体、执行UI更新事件）
        private BackgroundWorker backgroundWorker1 =null;
        public Form1()
        {
            InitializeComponent();

           
            backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
            //设置报告进度更新
            backgroundWorker1.WorkerReportsProgress = true;
            //注册线程主体方法
            backgroundWorker1.DoWork += new DoWorkEventHandler(backgroundWorker1_DoWork);
            //注册更新UI方法
            backgroundWorker1.ProgressChanged += new ProgressChangedEventHandler(backgroundWorker1_ProgressChanged);
            //backgroundWorker1.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.backgroundWorker1_RunWorkerCompleted);
        }

        //第二步：定义执行线程主体事件
        //线程主体方法
        public void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            //...执行线程任务

            //在线程中更新UI（通过ReportProgress方法）
            backgroundWorker1.ReportProgress(50, "This text was set safely by BackgroundWorker.");

            //...执行线程其他任务
        }
        //第三步：定义执行UI更新事件
        //UI更新方法
        public void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            this.textBox1.Text = e.UserState.ToString();
        }
        //之后，启动线程
        //启动backgroundWorker
        private void setTextBackgroundWorkerBtn_Click(object sender, EventArgs e)
        {
            this.backgroundWorker1.RunWorkerAsync();
        }
```

 

说明：C# Winform中执行异步任务时，BackgroundWorker是个不错的选择。它是EAP（Event based Asynchronous Pattern）思想的产物，DoWork用来执行异步任务，在任务执行过程中/执行完成后，我们可以通过ProgressChanged，ProgressCompleteded事件进行线程安全的UI更新。 需要注意的是：//设置报告进度更新 backgroundWorker1.WorkerReportsProgress = true; 默认情况下BackgroundWorker是不报告进度的，需要显示设置报告进度属性。

# 通过设置窗体属性，取消线程安全检查来避免"线程间操作无效异常"（非线程安全，建议不使用）

用法：将Control类的静态属性CheckForIllegalCrossThreadCalls为false。

我自己做的通用版

```
delegate void SetTextCallback(TextBox textBox, string text);
private void SetText(TextBox textBox, string text)
{
    // InvokeRequired required compares the thread ID of the 
    // calling thread to the thread ID of the creating thread. 
    // If these threads are different, it returns true. 
    if (textBox.InvokeRequired)//如果调用控件的线程和创建创建控件的线程不是同一个则为True
    {
        while (!textBox.IsHandleCreated)
        {
            //解决窗体关闭时出现“访问已释放句柄“的异常
            if (textBox.Disposing || textBox.IsDisposed)
                return;
        }
        SetTextCallback d = new SetTextCallback(SetText);
        textBox.BeginInvoke(d,  new object[] { textBox,text } );
    }
    else
    {
        textBox.Text = text;
    }
}
```
