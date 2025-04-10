---
layout: post
title:  wpf自定义依赖属性接收ObservableCollection消息
date:   2025-4-10 16:23:00 +0800
categories: ["c#", "Wpf"]
project: false
excerpt: wpf自定义依赖属性接收ObservableCollection消息
lang: zh
published: true
tag:
- c#
- wpf
- 依赖属性
- ObservableCollection
---

代码，重要的是添加事件处理。
```c#
public class MyControl : Control
{
    public MyControl()
    {
        Items = new ObservableCollection<string>();
    }

    public ObservableCollection<string> Items
    {
        get => (ObservableCollection<string>)GetValue(ItemsProperty);
        set => SetValue(ItemsProperty, value);
    }

    public static readonly DependencyProperty ItemsProperty =
        DependencyProperty.Register(
            nameof(Items),
            typeof(ObservableCollection<string>),
            typeof(MyControl),
            new PropertyMetadata(null, OnItemsChanged));

    private static void OnItemsChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
    {
        var control = (MyControl)d;
        var oldCollection = e.OldValue as INotifyCollectionChanged;
        var newCollection = e.NewValue as INotifyCollectionChanged;

        if (oldCollection != null)
            oldCollection.CollectionChanged -= control.OnCollectionChanged;
        
        if (newCollection != null)
            newCollection.CollectionChanged += control.OnCollectionChanged;
    }

    private void OnCollectionChanged(object sender, NotifyCollectionChangedEventArgs e)
    {
        // 根据不同的Action处理UI更新
        switch (e.Action)
        {
            case NotifyCollectionChangedAction.Add:
                UpdateUIForAddedItems(e.NewItems);
                break;
            case NotifyCollectionChangedAction.Remove:
                UpdateUIForRemovedItems(e.OldItems);
                break;
            case NotifyCollectionChangedAction.Reset:
                ResetUI();
                break;
            // 可根据需要处理其他动作
        }
    }

    private void UpdateUIForAddedItems(IList newItems)
    {
        foreach (var item in newItems)
            AddItemToUI(item.ToString());
    }

    private void AddItemToUI(string item)
    {
        // 实际UI更新逻辑，例如添加控件到Panel
    }
}

```