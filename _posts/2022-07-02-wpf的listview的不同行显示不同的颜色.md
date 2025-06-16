---
layout: post
title: "wpf的ListView的不同行显示不同的颜色"
date: "2022-07-02"
categories: ["计算机语言", "c"]
---

```
<ListView.ItemContainerStyle>
                            <Style TargetType="ListViewItem">
                                <!-- 如下的这个是要定义，不同的状态选择不同的颜色。-->
                                <Setter Property="Background" Value="{Binding Converter={StaticResource ColorConverter}}" />
                            </Style>
                        </ListView.ItemContainerStyle>
```

单独的{Binding}表示将整个数据绑定，在这里，指的是每一行的数据，而ColorConverter是一个转换器。
