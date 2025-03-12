---
layout: post
title: "wpf的ListBox中的每一项都有一个删除按钮。"
date: "2019-05-17"
categories: 
  - "c"
---

```
private void btnClear_Click(object sender, RoutedEventArgs e)
{
    Button clickedButton = (Button)sender;
    DailySessions.Items.Remove(clickedButton.DataContext as DailySession);
}

```

如上的这个经过测试是可以的，as DailySession可以不添加，原作者是说 ：You need the cast if DailySessions returns an ObservableCollection.
