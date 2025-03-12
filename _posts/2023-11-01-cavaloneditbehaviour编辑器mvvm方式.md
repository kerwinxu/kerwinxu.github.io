---
title: "c#AvalonEditBehaviour编辑器mvvm方式"
date: "2023-11-01"
categories: 
  - "c"
---

1. 创建一个扩展
    
    ```
    public sealed class AvalonEditBehaviour : Behavior<TextEditor>
       {
           public static readonly DependencyProperty InputTextProperty =
               DependencyProperty.Register("InputText", typeof(string), typeof(AvalonEditBehaviour),
               new FrameworkPropertyMetadata(default(string), FrameworkPropertyMetadataOptions.BindsTwoWayByDefault, PropertyChangedCallback));
    
           public string InputText
           {
               get { return (string)GetValue(InputTextProperty); }
               set { SetValue(InputTextProperty, value); }
           }
    
           protected override void OnAttached()
           {
               base.OnAttached();
               if (AssociatedObject != null)
               {
                   AssociatedObject.TextChanged += AssociatedObjectOnTextChanged;
               }
           }
    
           protected override void OnDetaching()
           {
               base.OnDetaching();
               if (AssociatedObject != null)
               {
                   AssociatedObject.TextChanged -= AssociatedObjectOnTextChanged;
               }
           }
    
           private void AssociatedObjectOnTextChanged(object sender, EventArgs eventArgs)
           {
               var textEditor = sender as TextEditor;
               if (textEditor != null)
               {
                   if (textEditor.Document != null)
                   {
                       InputText = textEditor.Document.Text;
                   }
               }
           }
    
           private static void PropertyChangedCallback(
           DependencyObject dependencyObject,
           DependencyPropertyChangedEventArgs dependencyPropertyChangedEventArgs)
           {
               var behavior = dependencyObject as AvalonEditBehaviour;
               if (behavior.AssociatedObject != null)
               {
                   var editor = behavior.AssociatedObject as TextEditor;
                   if (editor.Document != null)
                   {
                       var caretOffset = editor.CaretOffset;
                       editor.Document.Text = dependencyPropertyChangedEventArgs.NewValue.ToString();
                       editor.CaretOffset = caretOffset;
                   }
               }
           }
    
    
       }
    ```
    
     
2. 使用这个扩展，
    
    ```
    <avalonEdit:TextEditor x:Name="sqlTextEditor" SyntaxHighlighting="SQL"
                                               ShowLineNumbers="True"
                                               Grid.Row="0"  VerticalScrollBarVisibility="Visible" >
                            <i:Interaction.Behaviors>
                                <AvalonEdit2:AvalonEditBehaviour InputText="{Binding SQLInput, Mode=TwoWay}"/>
                            </i:Interaction.Behaviors>
    </avalonEdit:TextEditor>
    ```
    
    头部加上
    
    ```
    xmlns:avalonEdit="http://icsharpcode.net/sharpdevelop/avalonedit"
    ```
