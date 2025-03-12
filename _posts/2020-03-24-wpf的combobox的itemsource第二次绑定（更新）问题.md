---
layout: post
title: "WPF的Combobox的ItemSource第二次绑定（更新）问题"
date: "2020-03-24"
categories: 
  - "c"
---

我定义个 List<Student> stuList = new List<Student>();

 

我想第二次更新了stuList后，让Combobox也更新。

一种是将student类继承notifychanged接口（INotifyPropertyChanged ），然后把stuList的类型从list改observablecollection。这样数据源更新了，Combobox会自动更新数据。 另一种，是在btnSave\_Click这个事件里，加入强制刷新的操作。this.combobox1.Item.Refresh();

推荐前种做法，一劳永逸。
