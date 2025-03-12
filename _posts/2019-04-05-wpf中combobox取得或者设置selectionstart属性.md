---
title: "wpf中ComboBox取得或者设置SelectionStart属性"
date: "2019-04-05"
categories: 
  - "c"
---

```
var myTextBox = combobox1.Template.FindName("PART_EditableTextBox", combobox1) as TextBox;
int old_selection_start = myTextBox.SelectionStart;
int olc_selection_length = myTextBox.SelectionLength;

```

如上才能取得这个属性。
