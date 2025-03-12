---
layout: post
title: "wpf中listbox添加序号"
date: "2024-07-28"
categories: 
  - "c-计算机"
---

做一个转换器，IList有IndexOf方法。

```
public class IndexConverter : IMultiValueConverter
    {
        public object? Convert(object[] values, Type targetType, object parameter, CultureInfo culture)
        {
            dynamic item = values[0];
            IList list = (IList)values[1];
            if (list != null) { return list.IndexOf(item) + 1; }
            else return null;
           
        }

        public object[] ConvertBack(object value, Type[] targetTypes, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
```

xamxl页面

```
<!--显示序号-->
                                    <TextBlock Text="{Binding}" Margin="0,5">
                                        <TextBlock.DataContext>
                                            <MultiBinding Converter="{StaticResource IndexConverter}">
                                                <Binding/>
                                                <Binding RelativeSource="{RelativeSource AncestorType=ListBox}" Path="ItemsSource" />
                                            </MultiBinding>
                                        </TextBlock.DataContext>
                                    </TextBlock>
```
