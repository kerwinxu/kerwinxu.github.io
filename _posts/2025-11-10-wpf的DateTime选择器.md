---
layout: post
title: "wpf的DateTime选择器"
date: "2025-11-10"
categories: ["C#", "wpf"]
---

```xml
<UserControl x:Class="智能化GIS设备安装质量管控平台.Controls.DateTimePicker"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
             xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
             xmlns:local="clr-namespace:智能化GIS设备安装质量管控平台.Controls"
             mc:Ignorable="d"
             d:DesignHeight="450" d:DesignWidth="800">
    <UserControl.Resources>
        <Style x:Key="ToggleButtonStyle" TargetType="ToggleButton">
            <Setter Property="Background" Value="Transparent"></Setter>
            <Setter Property="BorderThickness" Value="0"></Setter>
            <Setter Property="ContentTemplate">
                <Setter.Value>
                    <DataTemplate>
                        <Path Width="20" Height="20" Stretch="Uniform" Stroke="Gray">
                            <Path.Data>
                                <PathGeometry Figures="M775.401372 509.382023A248.716458 248.716458 0 0 1 1023.82488 757.805531a248.716458 248.716458 0 0
1-248.423508 248.423509A248.716458 248.716458 0 0 1 526.976863 757.805531a248.716458 248.716458 0 0 1
248.424509-248.423508z m0 64.062042c-101.651613 0-184.288478 82.636865-184.288479 184.288479 0 101.650613
82.636865 184.361466 184.288479 184.361466 101.650613 0 184.288478-82.636865 184.288478-184.288479s-82.637865-184.288478-184.288478-184.288478zM601.863054
0.17512c17.696973 0 32.030521 14.333548 32.030522
32.031521v62.599293H798.803369c36.345783 0 65.817742 29.470959 65.817742
65.816742v279.57818h-64.062043V160.622676l-166.664492-0.364937v55.140568a32.031521 32.031521 0
1 1-64.062043 0v-55.360531l-246.156896-0.438925v55.872444a32.031521 32.031521 0 1 1-64.13503 0v-56.018419l-193.721865-0.5849-1.682712
620.65684 389.493379 1.7557v64.062042H65.816742A65.89073 65.89073 0 0 1 0
779.524816V160.622676c0-36.345783 29.544946-65.816742 65.817742-65.816742h193.794853v-62.599293a32.031521 32.031521 0 1 1
64.062042 0v62.599293h246.157896v-62.599293C569.832533 14.508668 584.164082 0.17512 601.862055 0.17512z m173.538318 620.437877c17.696973 0
32.030521 14.333548 32.030521 32.031521v73.129492h61.722443a32.031521 32.031521 0 1 1 0 64.063042h-93.388027a32.104509 32.104509 0 0
1-32.469446-32.031521V652.643519c0-17.696973 14.407536-32.030521 32.104509-32.030522zM195.989477 537.683182a49.509532 49.509532 0 1 1
49.581519 85.782327 49.509532 49.509532 0 0 1-49.581519-85.782327z m218.732587 0a49.509532 49.509532 0 1 1 49.582519 85.782327 49.509532 49.509532 0
0 1-49.581519-85.782327zM196.062465 344.326255a49.509532 49.509532 0 1 1 49.509531 85.782327 49.509532 49.509532 0 0 1-49.582519-85.782327z m218.659599
0a49.509532 49.509532 0 1 1 49.655507 85.855315 49.509532 49.509532 0 0 1-49.58152-85.782328z m212.297687 0a49.509532 49.509532 0 1 1 49.58152 85.782327
49.509532 49.509532 0 0 1-49.58152-85.782327z" ></PathGeometry>
                            </Path.Data>
                        </Path>
                    </DataTemplate>
                </Setter.Value>
            </Setter>
        </Style>

        <Style x:Key="ButtonStyle" TargetType="Button">
            <Setter Property="Background" Value="Transparent"></Setter>
            <Setter Property="BorderThickness" Value="0"></Setter>
            <Setter Property="ContentTemplate">
                <Setter.Value>
                    <DataTemplate>
                        <Path Width="20" Height="20" Stretch="Uniform" Stroke="Green">
                            <Path.Data>
                                <PathGeometry Figures="M886.745 249.567c-12.864-12.064-33.152-11.488-45.217 1.408L414.776 705.344l-233.12-229.696c-12.608-12.416-32.864-12.288-45.28 0.32-12.416 12.575-12.256 32.863 0.352 45.248l256.48 252.672c0.096 0.096 0.224 0.128 0.319 0.224 0.097 0.096 0.129 0.224 0.225 0.32 2.016 1.92 4.448 3.008 6.784 4.288 1.151 0.672 2.144 1.664 3.359 2.144 3.776 1.472 7.776 2.24 11.744 2.24 4.192 0 8.384-0.832 12.288-2.496 1.313-0.544 2.336-1.664 3.552-2.368 2.4-1.408 4.896-2.592 6.944-4.672 0.096-0.096 0.128-0.256 0.224-0.352 0.064-0.097 0.192-0.129 0.288-0.225l449.185-478.208C900.28 281.951 899.608 261.695 886.745 249.567z" ></PathGeometry>
                            </Path.Data>
                        </Path>
                    </DataTemplate>
                </Setter.Value>
            </Setter>
        </Style>
    </UserControl.Resources>
    <Viewbox>
        <Border CornerRadius="4">
            <Grid Background="Transparent">
                <Grid.RowDefinitions>
                    <RowDefinition></RowDefinition>
                    <RowDefinition></RowDefinition>
                </Grid.RowDefinitions>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition></ColumnDefinition>
                    <ColumnDefinition Width="auto"></ColumnDefinition>
                </Grid.ColumnDefinitions>

                <Border Grid.Row="0" BorderBrush="Gray" Grid.Column="0" BorderThickness="1" CornerRadius="2">
                    <TextBox BorderThickness="0" KeyUp="fullTimeControl_KeyUp" LostFocus="fullTimeControl_LostFocus" VerticalAlignment="Center" Margin="2" x:Name="fullTimeControl" Width="150" ></TextBox>
                </Border>

                <ToggleButton Grid.Row="0" Style="{StaticResource ToggleButtonStyle}" Grid.Column="1" Height="auto" Margin="2" x:Name="btn">
                </ToggleButton>
                <Grid Grid.Row="1" Background="Red" x:Name="gridChoice">
                    <Popup Focusable="True" StaysOpen="False" x:Name="mypopup" GotFocus="Popup_GotFocus" IsOpen="{Binding ElementName=btn,Path=IsChecked,UpdateSourceTrigger=PropertyChanged}" PlacementTarget="{Binding ElementName=gridChoice}" VerticalAlignment="Top">

                        <Grid Background="LightGray" Margin="0">
                            <Grid.RowDefinitions>
                                <RowDefinition Height="*"></RowDefinition>
                                <RowDefinition Height="auto"></RowDefinition>
                            </Grid.RowDefinitions>
                            <Grid.ColumnDefinitions>
                                <ColumnDefinition Width="auto"></ColumnDefinition>
                                <ColumnDefinition Width="*"></ColumnDefinition>
                                <ColumnDefinition Width="auto"></ColumnDefinition>
                            </Grid.ColumnDefinitions>
                            <Calendar Background="LightGray" x:Name="calendar" Grid.Column="0" Grid.ColumnSpan="3" Margin="0 -3 0 0"></Calendar>

                            <Path Width="20" Height="20" VerticalAlignment="Center" Margin="2 0" Grid.Row="1" Stretch="Uniform" Stroke="Gray">
                                <Path.Data>
                                    <PathGeometry Figures="M512 74.666667C270.933333 74.666667 74.666667 270.933333 74.666667 512S270.933333 949.333333 512 949.333333 949.333333 753.066667 949.333333 512 753.066667 74.666667 512 74.666667z m0 810.666666c-204.8 0-373.333333-168.533333-373.333333-373.333333S307.2 138.666667 512 138.666667 885.333333 307.2 885.333333 512 716.8 885.333333 512 885.333333z
M695.466667 567.466667l-151.466667-70.4V277.333333c0-17.066667-14.933333-32-32-32s-32 14.933333-32 32v238.933334c0 12.8 6.4 23.466667 19.2 29.866666l170.666667 81.066667c4.266667 2.133333 8.533333 2.133333 12.8 2.133333 12.8 0 23.466667-6.4 29.866666-19.2 6.4-14.933333 0-34.133333-17.066666-42.666666z" ></PathGeometry>
                                </Path.Data>
                            </Path>

                            <TextBox Grid.Row="1" Grid.Column="1" Margin="1 1 0 2" x:Name="textbox" VerticalAlignment="Center"></TextBox>
                            <Button Grid.Row="1" Grid.Column="2" PreviewMouseDown="Button_PreviewMouseDown" VerticalAlignment="Center" Style="{StaticResource ButtonStyle}" Width="30" Margin="2 1 1 2" ></Button>
                        </Grid>
                    </Popup>
                </Grid>
            </Grid>
        </Border>
    </Viewbox>
</UserControl>
```
