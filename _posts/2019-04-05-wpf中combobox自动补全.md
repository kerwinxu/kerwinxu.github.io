---
title: "wpf中Combobox自动补全"
date: "2019-04-05"
categories: 
  - "c"
---

```
/// <summary>
        /// 这个委托，实现过滤列表中的字符串效果。
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        public delegate bool fun_lst_filter(string str);
        private int Max_Combobox_items = 10;
        /// <summary>
        /// Combobox的自动补全，在combobox的xaml定义中添加 TextBoxBase.TextChanged="Combobox1_TextChanged" ，触发自动补全。
        /// 注意，combobox的如下3个属性要这样设置。
        /// IsTextSearchEnabled="False" 
        /// IsReadOnly="False" 
        /// IsEditable="True"
        /// </summary>
        /// <param name="cb">ComboBox控件</param>
        /// <param name="lst">要筛选的列表</param>
        /// <param name="lst_Filter">筛选函数，默认筛选函数是只要有匹配</param>
        public void combobox_auto_complete(ComboBox cb, List<string> lst, fun_lst_filter lst_Filter = null)
        {
            //我用异步实现自动补全。
            //将这个更新ui的操作转到异步后，快多了。优先级不能太快。
            this.Dispatcher.BeginInvoke(
                DispatcherPriority.ContextIdle, //优先级
                (ThreadStart)delegate ()  //如下就是一个委托，做了一个小线程。
                {
                    //先取得已经输入的文字。
                    string str_text = cb.Text;
                    //然后保留原先的编辑状态。
                    var myTextBox = cb.Template.FindName("PART_EditableTextBox", cb) as TextBox;
                    int old_selection_start = myTextBox.SelectionStart;
                    int olc_selection_length = myTextBox.SelectionLength;

                    //首先判断是否有字符吧，如果都为空，那么就不用判断啦，直接全部
                    if (str_text.Count() == 0)
                    {
                        //全部。
                        cb.ItemsSource = lst;
                        return;
                    }

                    //FindAll来过滤一下列表
                    //要判断是否有设置别的筛选函数
                    List<String> lst_tmp = new List<string>();
                    if (lst_Filter == null)
                    {
                        lst_tmp = lst.FindAll( n => n.IndexOf(str_text, StringComparison.CurrentCultureIgnoreCase) >= 0);
                        
                    }
                    else
                    {
                        lst_tmp = lst.FindAll(n => lst_Filter(n));

                    }

                    //更新下拉框。
                    //因为经常出现太多的项目，所以这里只显示最多Max_Combobox_items个项目吧。
                    lst_tmp = lst_tmp.Take(Max_Combobox_items).ToList();
       
                    //更新到combobox
                    cb.ItemsSource = lst_tmp;
                    //这里有个判断，就是当压根没有选项的时候，不打开下拉框啦
                    if (lst_tmp.Count > 0)
                    {
                        //这里表示有现象啦。
                        cb.IsDropDownOpen = true;//打开列表框。
                        //这里如果只有一个联系人，就设置自动补全上吧
                        if (lst_tmp.Count == 1)
                        {
                            cb.Text = lst_tmp[0];//就自动补全这个吧
                            cb.IsDropDownOpen = false;//我都已经补全了，关闭列表框。碍眼
                        }
                        else
                        {
                            //恢复原先的编辑状态。
                            myTextBox.SelectionStart = old_selection_start;
                            myTextBox.SelectionLength = olc_selection_length;
                        }
                    }
                    else
                    {
                        cb.IsDropDownOpen = false;//关闭列表框。
                    }
                });
        }

```
