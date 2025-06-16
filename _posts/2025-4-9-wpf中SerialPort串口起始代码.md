---
layout: post
title:  wpf中SerialPort串口起始代码
date:   2025-4-9 11:02:00 +0800
categories: ["计算机语言","c#"]
project: false
excerpt: wpf中SerialPort串口起始代码
lang: zh
published: true
tag:
- c#
- wpf
- SerialPort
- 串口
---

前端
```xml
<Window x:Class="THUIC心电系统软件.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:THUIC心电系统软件"
        mc:Ignorable="d"
        DataContext="{Binding Source={StaticResource locator},Path=Main}"
        xmlns:i="clr-namespace:System.Windows.Interactivity;assembly=System.Windows.Interactivity"
        xmlns:cmd="http://www.galasoft.ch/mvvmlight"
        
        Title="THUIC心电系统软件" Height="450" Width="800">
    <Window.Resources>
        <Style TargetType="TextBlock" BasedOn="{StaticResource MaterialDesignBody1TextBlock}">
            <Setter Property="VerticalAlignment" Value="Center" />
            <Setter Property="Margin" Value="5,0,5,0" />
        </Style>
        <Style TargetType="ComboBox" BasedOn="{StaticResource MaterialDesignComboBox}">
            <Setter Property="VerticalAlignment" Value="Center" />
            <Setter Property="Margin" Value="5,0,5,0" />
        </Style>
        <Style TargetType="Button" BasedOn="{StaticResource MaterialDesignFlatDarkBgButton}" >
            <Setter Property="VerticalAlignment" Value="Center" />
            <Setter Property="Margin" Value="5,0,5,0" />
        </Style>
    </Window.Resources>
    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="40" />
            <RowDefinition Height="1*" />
        </Grid.RowDefinitions>
        <StackPanel Orientation="Horizontal">
            <TextBlock Text="串口:" />
            <ComboBox Width="60"  ItemsSource="{Binding PortNames}" SelectedItem="{Binding PortName}">
                <!-- 绑定下拉框弹出事件-->
                <i:Interaction.Triggers>
                    <!--wpf的弹出下拉框是DropDownOpened-->
                    <i:EventTrigger EventName="DropDownOpened">
                        <cmd:EventToCommand Command="{Binding ShowPortNames}" PassEventArgsToCommand="True" />
                </i:EventTrigger>
                </i:Interaction.Triggers>
            </ComboBox>
            <TextBlock Text="波特率"/>
            <ComboBox Width="90" ItemsSource="{Binding Baudrates}" SelectedItem="{Binding BaudRate}" />
            <TextBlock Text="数据位" />
            <ComboBox Width="50" ItemsSource="{Binding Databitss}" SelectedItem="{Binding Databits}"/>
            <TextBlock Text="校验" />
            <ComboBox Width="80" ItemsSource="{Binding Parities}" SelectedItem="{Binding Parity}"/>
            <TextBlock Text="停止位" />
            <ComboBox Width="60" ItemsSource="{Binding StopBitss}" SelectedItem="{Binding StopBits}"/>
            <Button Content="{Binding ConnectText}" Command="{Binding Connect}" />
        </StackPanel>
        
    </Grid>
</Window>
```

后端
```c#
public class MainViewModel : ViewModelBase
{

    public MainViewModel() {
        BaudRate = 9600;
        Databits = 8;
        Parity = Parity.None;
        StopBits = StopBits.One;
        ConnectText = "打开";
    }

    #region 串口相关

    /// <summary>
    /// 串口
    /// </summary>
    private SerialPort serialPort = new SerialPort();


    private string[] portNames;

    public string[] PortNames
    {
        get { return portNames; }
        set { portNames = value; RaisePropertyChanged(() => PortNames); }
    }

    private string portName;
    /// <summary>
    /// 串口名称
    /// </summary>
    public string PortName
    {
        get { return portName; }
        set { portName = value; RaisePropertyChanged(() => PortName); }
    }

    private void _show_portnames(EventArgs args)
    {
        PortNames = SerialPort.GetPortNames();
        Debug.WriteLine($"显示串口:{string.Join(",",PortNames)}");
    }

    private RelayCommand<EventArgs> showPortNames;
    /// <summary>
    /// 
    /// </summary>
    public RelayCommand<EventArgs> ShowPortNames
    {
        get
        {
            if (showPortNames == null) showPortNames = new RelayCommand<EventArgs>(_show_portnames);
            return showPortNames;
        }
    }



    public int[] Baudrates
    {
        get { return new int[] {1200,4800,9600,19200,38400,57600,115200 }; }
    }

    private int baudrate;
    /// <summary>
    /// 波特率
    /// </summary>
    public int BaudRate
    {
        get { return baudrate; }
        set { baudrate = value; RaisePropertyChanged(() => BaudRate); }
    }
    
    public int[] Databitss
    {
        get
        {
            return new int[] { 5, 6, 7, 8 };
        }
    }

    private int databits;
    /// <summary>
    /// 数据位
    /// </summary>
    public int Databits
    {
        get { return databits; }
        set { databits = value; RaisePropertyChanged(() => Databits); }
    }

    private Parity[] parities1 = {Parity.None, Parity.Odd, Parity.Even };

    private string[] Parities2 = { "None", "Odd", "Even" };

    public Parity[] Parities
    {
        get { return parities1; }
    }

    private Parity parity;

    public Parity Parity
    {
        get { return parity; }
        set { parity = value; RaisePropertyChanged(() => Parity); }
    }

    public StopBits[] StopBitss
    {
        get { return new StopBits[] { StopBits.One, StopBits.Two, StopBits.OnePointFive }; }
    }

    private StopBits stopBits;

    public StopBits StopBits
    {
        get { return stopBits; }
        set { stopBits = value; RaisePropertyChanged(() => StopBits); }
    }

    private string connectText;

    public string ConnectText
    {
        get { return connectText; }
        set { connectText = value; RaisePropertyChanged(() => ConnectText); }
    }

    private void _connect()
    {
        try
        {
            if (ConnectText == "打开")
            {
                if (serialPort.IsOpen) serialPort.Close();
                serialPort.PortName = PortName;
                serialPort.BaudRate = BaudRate;
                serialPort.DataBits = Databits;
                serialPort.Parity = Parity;
                serialPort.StopBits = StopBits;
                serialPort.Open();
                // 这里看看是同步还是异步接收
                ConnectText = "关闭";
            }
            else
            {
                if (serialPort.IsOpen) serialPort.Close();
                ConnectText = "打开";
            }
        }
        catch (Exception ex)
        {
            MessageBox.Show(ex.Message);
            //throw;
        }

    }

    private RelayCommand connect;
    /// <summary>
    /// 
    /// </summary>
    public RelayCommand Connect
    {
        get
        {
            if (connect == null) connect = new RelayCommand(_connect);
            return connect;
        }
    }



    #endregion

}
```