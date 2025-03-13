---
layout: post
title: "wpf中datagrid单击可编辑"
date: "2025-02-02"
categories: 
  - "c"
---

```xml
<DataGrid.Resources>
    <Style TargetType="DataGridCell" BasedOn="{StaticResource {x:Type DataGridCell}}">
        <Style.Triggers>
            <MultiTrigger>
                <MultiTrigger.Conditions>
                    <Condition Property="IsMouseOver" Value="True" />
                    <Condition Property="IsReadOnly" Value="False" />
                </MultiTrigger.Conditions>
                <MultiTrigger.Setters>
                    <Setter Property="IsEditing" Value="True" />
                </MultiTrigger.Setters>
            </MultiTrigger>
        </Style.Triggers>
    </Style>
</DataGrid.Resources>
```
