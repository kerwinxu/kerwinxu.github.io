---
title: "wpf的ListView的排序"
date: "2023-01-23"
categories: 
  - "c"
---

两处，第一处xaml中添加事件声明，第二处在窗口代码中定义这个事件。

 

```
<Window x:Class="ListViewSort.MainWindow"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="MainWindow" Height="300" Width="300" Loaded="Window_Loaded">
    <Grid>
        <ListView GridViewColumnHeader.Click="GridViewColumnHeader_Click" Margin="2" ItemsSource="{Binding Path=DataList}" >
            <ListView.View>
                <GridView>
                    <GridViewColumn  Header="ID" DisplayMemberBinding="{Binding ID}" />
                    <GridViewColumn  Header="Name" DisplayMemberBinding="{Binding Name}" />
                </GridView>
            </ListView.View>
        </ListView>
    </Grid>
</Window>
```

 

```
private void GridViewColumnHeader_Click(object sender, RoutedEventArgs e) {
           ListView view = sender as ListView;
           if (view == null) {
               return;
           }
           if (e.OriginalSource is GridViewColumnHeader) {
               //获取点击列
               GridViewColumn clickedColumn = (e.OriginalSource as GridViewColumnHeader)?.Column;
               if (clickedColumn != null) {
                   //获取该列绑定的属性
                   string bindingProperty = (clickedColumn.DisplayMemberBinding as Binding)?.Path.Path;
                   if (bindingProperty == null) {
                       return;
                   }
                   SortDescriptionCollection sdc = view.Items.SortDescriptions;
                   ListSortDirection sortDirection = ListSortDirection.Ascending;
                   foreach (var sd in sdc) {
                       if (sd.PropertyName.Equals(bindingProperty)) {
                           //改变排序方向
                           sortDirection = (ListSortDirection) ((((int) sd.Direction) + 1) % 2);
                           //取得排序方向后，删除当前的SortDescription
                           sdc.Remove(sd);
                           break;
                       }
                   }
                   //添加新的SortDescription到SortDescriptions首位，使之生效
                   sdc.Insert(0,new SortDescription(bindingProperty, sortDirection));
               }
           }
       }
```
