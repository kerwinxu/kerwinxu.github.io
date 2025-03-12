---
title: "wpf中富文本编辑框AvalonEdit的使用"
date: "2019-05-08"
categories: 
  - "c"
---

1. 下载安装 AvalonEdit ，我用nuget来安装。
2. 在xaml文件中添加如下命名控件。
    1. xmlns:avalonEdit="http://icsharpcode.net/sharpdevelop/avalonedit"
3. 在xaml文件中添加如下代码就可以
    1. ```
                    <avalonEdit:TextEditor
                        xmlns:avalonEdit="http://icsharpcode.net/sharpdevelop/avalonedit"  
                        Name="MyAvalonEdit"
                        FontFamily="Consolas"
                        FontSize="10pt" 
                        ShowLineNumbers="True" 
                        LineNumbersForeground="#FF2B91AF" />
        ```
        
4. 如果需要语法高亮，就建立一个.xshd文件，比如sql.xshd ，然后将这个文件的生成操作设置成，内嵌的资源。
5. 然后在代码中
    1. ```
        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            using (var stream = System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream("DefaultNamespace.Folder.sql.xshd"))
            {
                using (var reader = new System.Xml.XmlTextReader(stream))
                {
                    MyAvalonEdit.SyntaxHighlighting = 
                        ICSharpCode.AvalonEdit.Highlighting.Xshd.HighlightingLoader.Load(reader, 
                        ICSharpCode.AvalonEdit.Highlighting.HighlightingManager.Instance);
                }
            }
        }
        ```
