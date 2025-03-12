---
layout: post
title: "c#从sysListview中取得相关的内容"
date: "2021-04-11"
categories: 
  - "c"
---

```
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Drawing.Printing;
//using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Windows.Automation;
//using System.Threading.Tasks;
using System.Windows.Forms;

namespace 自动打印
{
    public partial class Form1 : Form
    {
        const int buffer_size = 1024;

        private const uint LVM_FIRST = 0x1000;
        private const uint LVM_GETITEMCOUNT = LVM_FIRST + 4;  // 获得总行数
        private const uint LVM_GETITEMW = LVM_FIRST + 75;    // 获得每一项
        private const uint HDM_GETITEMCOUNT = 0x1200;//获取列表列数
        private static uint WM_GETTEXT = 0x000D; //取得控件的值。


        [DllImport("user32.dll", EntryPoint = "FindWindow", SetLastError = true)]
        private static extern IntPtr FindWindow(string lpClassName, string lpWindowName);

        [DllImport("user32.dll", EntryPoint = "FindWindowEx", SetLastError = true)]
        private static extern IntPtr FindWindowEx(IntPtr hwndParent, IntPtr hwndChildAfter, string lpszClass, string lpszWindow);

        [DllImport("user32.dll", EntryPoint = "SendMessage", SetLastError = true, CharSet = CharSet.Auto)]
        private static extern int SendMessage(IntPtr hwnd, uint wMsg, int wParam, StringBuilder lParam);

        [DllImport("user32.dll", EntryPoint = "SendMessage", SetLastError = true, CharSet = CharSet.Auto)]
        private static extern int SendMessage2(IntPtr hwnd, uint wMsg, int wParam, int lParam);

        [DllImport("user32.dll", EntryPoint = "SetForegroundWindow", SetLastError = true)]
        private static extern void SetForegroundWindow(IntPtr hwnd);


        [DllImport("user32", EntryPoint = "GetDlgCtrlID")]
        public static extern int GetDlgCtrlID(IntPtr hwnd);

        [DllImport("user32.dll", SetLastError = true)] 
        static extern IntPtr GetWindow(IntPtr hWnd, GetWindowCmd uCmd);
        ///

       

        /// 窗口与要获得句柄的窗口之间的关系。
        ///

        enum GetWindowCmd : uint

        {           
            ///
            /// 返回的句柄标识了在Z序最高端的相同类型的窗口。
            /// 如果指定窗口是最高端窗口，则该句柄标识了在Z序最高端的最高端窗口；
            /// 如果指定窗口是顶层窗口，则该句柄标识了在z序最高端的顶层窗口：
            /// 如果指定窗口是子窗口，则句柄标识了在Z序最高端的同属窗口。
            ///
            GW_HWNDFIRST = 0,            ///

            /// 返回的句柄标识了在z序最低端的相同类型的窗口。
            /// 如果指定窗口是最高端窗口，则该柄标识了在z序最低端的最高端窗口：
            /// 如果指定窗口是顶层窗口，则该句柄标识了在z序最低端的顶层窗口；
            /// 如果指定窗口是子窗口，则句柄标识了在Z序最低端的同属窗口。
            ///
            GW_HWNDLAST = 1,            ///


            /// 返回的句柄标识了在Z序中指定窗口下的相同类型的窗口。
            /// 如果指定窗口是最高端窗口，则该句柄标识了在指定窗口下的最高端窗口：
            /// 如果指定窗口是顶层窗口，则该句柄标识了在指定窗口下的顶层窗口；
            /// 如果指定窗口是子窗口，则句柄标识了在指定窗口下的同属窗口。
            ///
            GW_HWNDNEXT = 2,            ///


            /// 返回的句柄标识了在Z序中指定窗口上的相同类型的窗口。
            /// 如果指定窗口是最高端窗口，则该句柄标识了在指定窗口上的最高端窗口；
            /// 如果指定窗口是顶层窗口，则该句柄标识了在指定窗口上的顶层窗口；
            /// 如果指定窗口是子窗口，则句柄标识了在指定窗口上的同属窗口。
            ///
            GW_HWNDPREV = 3,            ///


            /// 返回的句柄标识了指定窗口的所有者窗口（如果存在）。
            /// GW_OWNER与GW_CHILD不是相对的参数，没有父窗口的含义，如果想得到父窗口请使用GetParent()。
            /// 例如：例如有时对话框的控件的GW_OWNER，是不存在的。
            ///
            GW_OWNER = 4,            ///


            /// 如果指定窗口是父窗口，则获得的是在Tab序顶端的子窗口的句柄，否则为NULL。
            /// 函数仅检查指定父窗口的子窗口，不检查继承窗口。
            ///
            GW_CHILD = 5,            ///


            /// （WindowsNT 5.0）返回的句柄标识了属于指定窗口的处于使能状态弹出式窗口（检索使用第一个由GW_HWNDNEXT 查找到的满足前述条件的窗口）；
            /// 如果无使能窗口，则获得的句柄与指定窗口相同。
            ///
            GW_ENABLEDPOPUP = 6

        }     
        
        /*GetWindowCmd指定结果窗口与源窗口的关系，它们建立在下述常数基础上：

              GW_CHILD

              寻找源窗口的第一个子窗口

              GW_HWNDFIRST

              为一个源子窗口寻找第一个兄弟（同级）窗口，或寻找第一个顶级窗口

              GW_HWNDLAST

              为一个源子窗口寻找最后一个兄弟（同级）窗口，或寻找最后一个顶级窗口

              GW_HWNDNEXT

              为源窗口寻找下一个兄弟窗口

              GW_HWNDPREV

              为源窗口寻找前一个兄弟窗口

              GW_OWNER

              寻找窗口的所有者

 */


        System.Drawing.Image image = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void btn_print_Click(object sender, EventArgs e)
        {
            //这里首先取得窗体
            //然后求出窗口的控件 Afx:400000:b:10003:6:26da135f
            IntPtr maindHwnd = FindWindow(null, "义务CEL - 快递业务管理系统 ∷ genzong:genzong"); //
            if (maindHwnd == IntPtr.Zero)
            {
                MessageBox.Show("没有发现相关窗体");
                return;
            }

            //如下是获得几个
            //如下是获得下一家
            StringBuilder buffer_nextCompany = new StringBuilder(buffer_size);
            SendMessage(GetChildHWnd(maindHwnd, 0x000004B4), WM_GETTEXT, buffer_size, buffer_nextCompany);
            Trace.WriteLine("下一家："+buffer_nextCompany.ToString());
            //发送日期
            StringBuilder buffer_sendData = new StringBuilder(buffer_size);
            SendMessage(GetChildHWnd(maindHwnd, 0x00000620), WM_GETTEXT, buffer_size, buffer_sendData);
            Trace.WriteLine("发送日期：" + buffer_sendData.ToString());
            //快件数量
            StringBuilder buffer_count = new StringBuilder(buffer_size);
            SendMessage(GetChildHWnd(maindHwnd, 0x000004D4), WM_GETTEXT, buffer_size, buffer_count);
            //这里快件列表:共1122件 格式是这个，
            //
            int i_start = buffer_count.ToString().IndexOf("共"); 
            int i_end = buffer_count.ToString().LastIndexOf("件");
            int i_count = Convert.ToInt32(buffer_count.ToString().Substring(i_start+1,i_end-i_start-1));
            Trace.WriteLine("快件数量：" + i_count.ToString());

            //然后如下是取得 sysListview 中的内容
            //然后这里要遍历这个里边所有的项目，直到最后一项。
            
            
            //其实，我这个只是读取两项就可以了，一个是起始的第一个，一个是最后一个

            var lstview_data = GetListViewItmeValue(maindHwnd, 0x0000043D);
            string str_liuyongchuan = lstview_data[0,6];
            string str_total_w = lstview_data[lstview_data.GetLength(0)-1, 4]; //总重量

            Trace.WriteLine("留用串：" + str_liuyongchuan);
            Trace.WriteLine("总重量：" + str_total_w);

            //这里保存图片吧
            if (image != null)
            {
                image.Dispose();
                image = null;
            }
            image = Image.FromFile("底图.png"); // 在这个图片上绘制
            Graphics graphics = Graphics.FromImage(image);

            // 用这个字体
            Font DrawFont = new Font("Arial", 24);
            SolidBrush brush = new SolidBrush(System.Drawing.Color.Black);

            //位置的起始
            int w_s = 220;
            int w_e = 736;

            //打印第一个
            var size1 = graphics.MeasureString(str_liuyongchuan, DrawFont);
            graphics.DrawString(str_liuyongchuan, DrawFont, brush, new PointF(w_s + (w_e-size1.Width-w_s)/2 ,200 ));

            var size2 = graphics.MeasureString(i_count.ToString(), DrawFont);
            graphics.DrawString(i_count.ToString(), DrawFont, brush, new PointF(w_s + (w_e - size2.Width - w_s) / 2, 310));

            var size3 = graphics.MeasureString(str_total_w, DrawFont);
            graphics.DrawString(str_total_w, DrawFont, brush, new PointF(w_s + (w_e - size3.Width - w_s) / 2, 420));

            var size4 = graphics.MeasureString(buffer_nextCompany.ToString(), DrawFont);
            graphics.DrawString(buffer_nextCompany.ToString(), DrawFont, brush, new PointF(w_s + (w_e - size4.Width - w_s) / 2, 530));

            var size5 = graphics.MeasureString(buffer_sendData.ToString(), DrawFont);
            graphics.DrawString(buffer_sendData.ToString(), DrawFont, brush, new PointF(w_s + (w_e - size5.Width - w_s) / 2, 640));

            graphics.Dispose();

            image.Save("a.png");

            //如下开始打印
            PrintDocument pd = new PrintDocument();
            pd.PrintPage += Pd_PrintPage;

            pd.Print();
            Trace.WriteLine("调用打印");
        }

        private void Pd_PrintPage(object sender, PrintPageEventArgs e)
        {

            e.Graphics.DrawImage(image, 0, 0);
            e.HasMorePages = false; //打印一张。

            //throw new NotImplementedException();
        }

        private string get_value(IntPtr maindHwnd, string lpClassName, string lpWindowName)
        {

            IntPtr h = FindWindowEx(maindHwnd, IntPtr.Zero, lpClassName, lpWindowName);
            if (h == IntPtr.Zero)
            {
                return string.Empty;
            }

            const int buffer_size = 1024;
            StringBuilder buffer = new StringBuilder(buffer_size);
            SendMessage(h, WM_GETTEXT, buffer_size, buffer);

            return buffer.ToString();

        }


        IntPtr mIDHWnd;

        /// <summary>
        /// 根据控件id取得控件句柄
        /// </summary>
        /// <param name="mHwnd"></param>
        /// <param name="ID"></param>
        /// <returns></returns>
        private IntPtr GetChildHWnd(IntPtr mHwnd, int ID)
        {
            while (mHwnd != IntPtr.Zero)
            {
                int id_tmp = GetDlgCtrlID(mHwnd);
                if (id_tmp == ID)
                {
                    mIDHWnd = mHwnd;
                    break;
                }

                //如果有子控件
                IntPtr mChildHWnd = GetWindow(mHwnd, GetWindowCmd.GW_CHILD);
                if (mChildHWnd != IntPtr.Zero)
                {
                    GetChildHWnd(mChildHWnd, ID);
                }

                //下一个
                mHwnd = GetWindow(mHwnd, GetWindowCmd.GW_HWNDNEXT);

            }

            return mIDHWnd;

        }

        /// <summary>
        /// 列表的总行数
        /// </summary>
        /// <param name="AHandle"></param>
        /// <returns></returns>
        public int ListView_GetItemCount(IntPtr handle)
        {
            return SendMessage2(handle, LVM_GETITEMCOUNT, 0, 0);
        }

        /// <summary>  
        /// LV列表总列数
        /// </summary>
        private int ListView_GetItemCols(IntPtr handle)
        {
            IntPtr h_sysListview_header = FindWindowEx(handle, IntPtr.Zero, "SysHeader32", null);

            return SendMessage2(h_sysListview_header, HDM_GETITEMCOUNT, 0, 0);
        }

        /// <summary>
        /// 从内存中读取指定的LV控件的文本内容
        /// </summary>
        /// <param name="maindHwnd"></param>
        /// <param name="ID"></param>
        /// <returns></returns>
        private string[,] GetListViewItmeValue(IntPtr maindHwnd,int ID)
        {

            IntPtr h_sysListview = GetChildHWnd(maindHwnd, ID);

            // Get the AutomationElement that represents the window handle...
            AutomationElement el = AutomationElement.FromHandle(h_sysListview);

            // Walk the automation element tree using content view, so we only see
            // list items, not scrollbars and headers. (Use ControlViewWalker if you
            // want to traverse those also.)
            TreeWalker walker = TreeWalker.ContentViewWalker;


            Trace.WriteLine("得到SysListView32控件的句柄：" + h_sysListview.ToString());

            int rows = ListView_GetItemCount(h_sysListview);
            Trace.WriteLine("sysListview中行数：" + rows.ToString());


            int cols = ListView_GetItemCols(h_sysListview);
            Trace.WriteLine("sysListview中列数：" + cols.ToString());


            string[,] tempStr = new string[rows, cols];//二维数组:保存LV控件的文本信息

            int i = 0, j = 0;

            for (AutomationElement child = walker.GetFirstChild(el); child != null;  child = walker.GetNextSibling(child))
            {
                j = 0;
                // 这里试试是否可以知道那一列的数据
                for (AutomationElement child2 = walker.GetFirstChild(child); child2 != null; child2 = walker.GetNextSibling(child2))
                {
                    tempStr[i, j] = child2.Current.Name;
                    j++;
                    Trace.Write(child2.Current.Name + "\t");
                }
                Trace.Write("\n");
                i++;

                //Trace.WriteLine(child.Current.Name);
                // Print out the type of the item and its name
                //Console.WriteLine("item {0} is a \"{1}\" with name \"{2}\"", i++, child.Current.LocalizedControlType, child.Current.Name);
            }


            return tempStr;

            
        }

    }
}

```
