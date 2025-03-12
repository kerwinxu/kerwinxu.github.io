---
layout: post
title: "WPF的MVVMLight总结"
date: "2021-10-22"
categories: 
  - "c"
---

# 介绍MVVM模式

[![](/assets/image/default/167509-20170114191102681-2116055667.png)](http://127.0.0.1/?attachment_id=4136)

1. View负责前端展示，与ViewModel进行数据和命令的交互。
2. ViewModel，负责前端视图业务级别的逻辑结构组织，并将其反馈给前端。
3. Model，主要负责数据实体的结构处理，与ViewModel进行交互。

# 步骤

## 安装 MVVMLight

从nuget中安装就可以了。

## 建立文件夹

也就是建模Model、View、ViewModel三层文件夹

## 代码

### Model层

```
using GalaSoft.MvvmLight;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MVVMLightDemo.Model
{
    public class WelcomeModel : ObservableObject // 这个父类的作用就是保证能够检测属性是否被改变。它实现了 INotifyPropertyChanged接口
    {
        private String introduction;
        /// <summary>
        /// 欢迎词
        /// </summary>
        public String Introduction
        {
            get { return introduction; }
            set { introduction = value; RaisePropertyChanged(()=>Introduction); }
        }
    }
}
```

### VideModel

这个ViewModelBase是有一个Set方法的，简单理解就是不用自己在ViewModel实现INotifyPropertyChanged，然后在属性赋值时通知了，这样调用 Set("Welcome",ref welcome, value)

```
using GalaSoft.MvvmLight;
using MVVMLightDemo.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MVVMLightDemo.ViewModel
{
    public class WelcomeViewModel:ViewModelBase
    {
        /// <summary>
        /// 构造函数
        /// </summary>
        public WelcomeViewModel()
        {
            Welcome = new WelcomeModel() { Introduction = "Hello World！" };
        }
        #region 属性

        private WelcomeModel welcome;
        /// <summary>
        /// 欢迎词属性
        /// </summary>
        public WelcomeModel Welcome
        {
            get { return welcome; }
            set { welcome = value; RaisePropertyChanged(()=>Welcome); }
        }
        #endregion
    }
}
```

### View层

我这里跟App.xaml放在一层吧，

```
<Window x:Class="MVVMLightDemo.View.WelcomeView"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="WelcomeView" Height="300" Width="300">
    <Grid>
        <StackPanel VerticalAlignment="Center" HorizontalAlignment="Center" >
            <TextBlock Text="{Binding Welcome.Introduction}" FontSize="30" ></TextBlock>
        </StackPanel>
    </Grid>
</Window>
```

如果不是放在一层，其这个是启动窗口，需要如下这样子，

1. 更改App.xaml中的StartupUri="xxx.xaml" 为Startup="Application\_Startup"
2. 在App.xaml.cs中添加Application\_Startup方法
    
    ```
    private void Application_Startup(object sender, StartupEventArgs e)
       {
           Application.Current.StartupUri = new Uri("View/UserInfoWindow.xaml", UriKind.Relative);//View目录下
       }
    ```
    
     

### 修改构造器文件ViewModelLocator.cs

将新添加的viewmodel添加到构造器中。

```
/*
  In App.xaml:
  <Application.Resources>
      <vm:ViewModelLocator xmlns:vm="clr-namespace:WpfApp1"
                           x:Key="Locator" />
  </Application.Resources>
  
  In the View:
  DataContext="{Binding Source={StaticResource Locator}, Path=ViewModelName}"

  You can also use Blend to do all this with the tool's support.
  See http://www.galasoft.ch/mvvm
*/

using GalaSoft.MvvmLight;
using GalaSoft.MvvmLight.Ioc;
using Microsoft.Practices.ServiceLocation;

namespace WpfApp1.ViewModel
{
    /// <summary>
    /// This class contains static references to all the view models in the
    /// application and provides an entry point for the bindings.
    /// </summary>
    public class ViewModelLocator
    {
        /// <summary>
        /// Initializes a new instance of the ViewModelLocator class.
        /// </summary>
        public ViewModelLocator()
        {
            ServiceLocator.SetLocatorProvider(() => SimpleIoc.Default);

            ////if (ViewModelBase.IsInDesignModeStatic)
            ////{
            ////    // Create design time view services and models
            ////    SimpleIoc.Default.Register<IDataService, DesignDataService>();
            ////}
            ////else
            ////{
            ////    // Create run time view services and models
            ////    SimpleIoc.Default.Register<IDataService, DataService>();
            ////}

            SimpleIoc.Default.Register<MainViewModel>();
            SimpleIoc.Default.Register<WelcomeViewModel>();

        }

        public MainViewModel Main
        {
            get
            {
                return ServiceLocator.Current.GetInstance<MainViewModel>();
            }
        }

        public WelcomeViewModel Welcome
        {
            get
            {
                return ServiceLocator.Current.GetInstance<WelcomeViewModel>();
            }
        }
        
        public static void Cleanup()
        {
            // TODO Clear the ViewModels
        }
    }
}
```

这样每个ViewModel就有一个实例在构造器中，构造器本身是在 App.xaml 中启动的，另外关于这个文件的StartupUri是启动窗口。

```
<Application x:Class="WpfApp1.App" xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" 
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" 
             xmlns:local="clr-namespace:WpfApp1" 
             StartupUri="WelcomeView.xaml" 
             xmlns:d="http://schemas.microsoft.com/expression/blend/2008" d1p1:Ignorable="d" xmlns:d1p1="http://schemas.openxmlformats.org/markup-compatibility/2006">
    <Application.Resources>
        <ResourceDictionary>
            <vm:ViewModelLocator x:Key="Locator" d:IsDataSource="True" xmlns:vm="clr-namespace:WpfApp1.ViewModel" />
        </ResourceDictionary>
    </Application.Resources>
</Application>
```

### 更改数据源

更改 WelcomeView.xaml 中的 DataContext ，就是数据源。

```
<Window x:Class="WpfApp1.View.WelcomeView"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:WpfApp1.View"
        mc:Ignorable="d"
        DataContext="{Binding Source={StaticResource Locator}, Path=Welcome}"
        Title="WelcomeView" Height="450" Width="800">
    <Grid>
        <StackPanel VerticalAlignment="Center" HorizontalAlignment="Center" >
            <TextBlock Text="{Binding Welcome.Introduction}" FontSize="30" ></TextBlock>
        </StackPanel>
    </Grid>
</Window>
```

 

## 小总结

运行机制

- App.xaml 中重要的是2点
    - 启动 ViewModelLocator
    - 设置 StartupUri , 这个是启动视图View
- ViewModelLocator 构造器做如下几点
    - 注册所有的视图模型ViewModel
    - 创建视图模型的单例。
- View 视图，也就是用户看到的界面部分。
    - 数据源绑定ViewModelLocator 里创建的视图模型的单例。
- ViewModel ， 视图和模型之间的桥梁的，继承自 ViewModelBase ，数据改变后会通知其他的。
    - RaisePropertyChanged(()=>属性) ; 属性改变后会通知其他的。
- Model ， 模型继承自 ObservableObject  ，实现 INotifyPropertyChanged 接口，数据改变后会通知其他的。

 

# 命令

命令是解耦ViewModel和View之间的行为，比如原先是这样子的

View <-> ViewModel <-> Model ,

现在是这样子

View <-> 命令 <-> ViewModel <-> Model

 

## ICommand 接口

ICommand 公开了两个方法（Execute 及 CanExecute）和一个事件（CanExecuteChanged）

无参数 new RelayCommand(() => ExcuteValidForm(),CanExcute)

有一个参数

- CommandParameter="{Binding ElementName=ArgStrFrom,Path=Text}" ，在View上参数这样传递
- new RelayCommand<String>((p) => ExecutePassArgStr(p)); 然后在ViewModel上这样

多个参数，

怎么说呢，这些参数全部可以在后台的ViewModel的，我直接从后台读取就是了。

 

# 多线程

wpf的多线程跟winform的不一样，ViewModel 不从 DispatcherObject 继承。它们是执行 INotifyPropertyChanged 接口的 Plain Old CLR Objects (POCO)。

简单讲，就是在wpf的多线程中是如下做的

1. DispatcherHelper.Initialize(); 这个是初始化
2. DispatcherHelper.CheckBeginInvokeOnUI(() => 在多线程中是这样访问界面的。

 

# Messenger

不同的View，ViewModel 之间传送消息的，分两步

1. 接收方  ：Messenger.Default.Register<String>(this, "ViewAlert", ShowReceiveInfo);
    - ViewAlert 是token，唯一的标识符，区别不同消息的
    - ShowReceiveInfo是消息的处理方法。
2. 发送方 ：Messenger.Default.Send<String>("ViewModel通知View弹出消息框", "ViewAlert"); //注意：token参数一致
    - <String> 泛型，表示消息处理函数的参数的，
    - "ViewModel通知View弹出消息框" ，传递的消息内容。
    - "ViewAlert"， 唯一的标识符，

多线程和Messenger的区别，多线程是跨线程更改数据的，而Messager是跨界面来传递消息的。
