---
title: "wpf中DataGrid的自动行号"
date: "2023-04-29"
categories: 
  - "c"
---

做一个转换器

```
public  class RowToIndexConv: IValueConverter
{
    public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
    {
        DataGridRow row = value as DataGridRow;
        return $"{row.GetIndex() + 1}";
    }

    public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}
```

 

然后在xaml中

```
 <DataGrid>
     <DataGrid.Columns>
                <DataGridTextColumn Header="顺序"
                                    IsReadOnly="True"
                                    Binding="{Binding RelativeSource={RelativeSource AncestorType=DataGridRow},Converter={StaticResource RowToIndexConv}}"/>

                <DataGridTextColumn Header="规则内容"
                                    Binding="{Binding Text,Mode=TwoWay}"
                                    Width="2*"
                                    IsReadOnly="False"
                                    ></DataGridTextColumn>
                <DataGridTextColumn Header="捕获内容"
                                    Binding="{Binding Result}"
                                    Width="3*"
                                    IsReadOnly="True">

                </DataGridTextColumn>
                <DataGridTextColumn Header="备注"
                                    Binding="{Binding Remark,Mode=TwoWay}"
                                    Width="2*"
                                    IsReadOnly="False"
                                    ></DataGridTextColumn>
            </DataGrid.Columns>
            

</DataGrid>
```
