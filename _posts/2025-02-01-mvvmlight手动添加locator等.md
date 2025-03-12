---
layout: post
title: "mvvmlight手动添加locator等"
date: "2025-02-01"
categories: 
  - "c"
---

```
public class ViewModelLocator
    {
        /// <summary>
        /// Initializes a new instance of the ViewModelLocator class.
        /// </summary>
        public ViewModelLocator()
        {
            ServiceLocator.SetLocatorProvider(() => SimpleIoc.Default);

            SimpleIoc.Default.Register<MainViewModel>();
        }

        public MainViewModel Main
        {
            get
            {
                return ServiceLocator.Current.GetInstance<MainViewModel>();
            }
        }

        public static void Cleanup()
        {
            // TODO Clear the ViewModels
        }
    }
```

添加

```
public  class MainViewModel:ViewModelBase
{

}
```

修改App.xaml

```
<Application x:Class="FLIZPONE.App"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:local="clr-namespace:FLIZPONE"
             xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
             d1p1:Ignorable="d" 
             xmlns:d1p1="http://schemas.openxmlformats.org/markup-compatibility/2006"
             xmlns:vw ="clr-namespace:FLIZPONE.ModelView"
             StartupUri="MainWindow.xaml">
    <Application.Resources>
        <vw:ViewModelLocator x:Key="locator" d:IsDataSource="True" />

    </Application.Resources>
</Application>
```

 

在MainWindow.xaml中添加

```
DataContext="{Binding Source={StaticResource locator},Path=Main}"
```
