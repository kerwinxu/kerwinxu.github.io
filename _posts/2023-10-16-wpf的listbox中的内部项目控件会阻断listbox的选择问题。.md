---
layout: post
title: "wpf的listbox中的内部项目控件会阻断listbox的选择问题。"
date: "2023-10-16"
categories: ["计算机语言", "c"]
---

比如内部的一个文本输入控件，消息传递到文本控件，就不往上层传递了。解决

```c#
/// <summary>
   /// 选择listbox内部的按钮，listbox也设置这一项为当前项目
   /// </summary>
   public class ListBoxService
   {
       #region AutoSelect Property

       public static readonly DependencyProperty AutoSelectProperty = DependencyProperty.RegisterAttached("AutoSelect", typeof(bool), typeof(ListBoxService), new PropertyMetadata(OnAutoSelectPropertyChanged));

       public static bool GetAutoSelect(DependencyObject element)
       {
           if (element == null)
               return false;

           return (bool)element.GetValue(AutoSelectProperty);
       }

       public static void SetAutoSelect(DependencyObject element, bool value)
       {
           if (element == null)
               return;

           element.SetValue(AutoSelectProperty, value);
       }

       #endregion

       private static void OnAutoSelectPropertyChanged(DependencyObject element, DependencyPropertyChangedEventArgs e)
       {
           if (!(element is UIElement))
               return;

           if ((bool)e.NewValue)
               (element as UIElement).GotFocus += new RoutedEventHandler(OnElementGotFocus);
           else
               (element as UIElement).GotFocus -= new RoutedEventHandler(OnElementGotFocus);
       }

       private static void OnElementGotFocus(object sender, RoutedEventArgs e)
       {
           Debug.Assert(e.OriginalSource is DependencyObject);

           ListBoxItem item = (e.OriginalSource as DependencyObject).FindAncestor<ListBoxItem>();
           if (item != null)
               item.IsSelected = true;
           else
               Debug.WriteLine(string.Format("Cannot find ListBoxItem from {0}", sender));
       }
   }
```

```
/// <summary>
    /// DependencyObject的一个扩展方法，方便取得控件的。
    /// </summary>
    public static class Extension
    {
        /// <summary>
        /// 
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="element"></param>
        /// <returns></returns>
        public static T FindAncestor<T>(this DependencyObject element) where T : DependencyObject
        {
            if (element == null)
                return null;

            DependencyObject parent = GetParent(element);

            if (parent == null)
                return null;

            if (parent is T)
                return parent as T;

            return parent.FindAncestor<T>();
        }

        private static DependencyObject GetParent(DependencyObject element)
        {
            if (element is FrameworkElement)
            {
                FrameworkElement frameworkElement = element as FrameworkElement;
                if (frameworkElement.Parent != null)
                    return frameworkElement.Parent;
                else if (frameworkElement.TemplatedParent != null)
                    return frameworkElement.TemplatedParent;
            }

            return VisualTreeHelper.GetParent(element);
        }
    }
```

最后在视图中

```
<Window.Resources>
    <Style TargetType="{x:Type ListBox}">
        <Setter Property="patch:ListBoxService.AutoSelect" Value="True"/>
    </Style>
</Window.Resources>
```
