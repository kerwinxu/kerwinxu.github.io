---
layout: post
title: "wpf中combobox的背景色更改"
date: "2023-11-05"
categories: 
  - "c"
---

```
<!-- 禁用情况下控件的颜色 -->
<Color x:Key="DisabledControlLightColor">#FFE8EDF9</Color>
<Color x:Key="DisabledControlDarkColor">#FFC5CBF9</Color> <!-- 背景色 -->
<Color x:Key="DisabledForegroundColor">#FF888888</Color>  <!-- 前景色-->

<!-- 当前选择的-->
<Color x:Key="SelectedBackgroundColor">#FFC5CBF9</Color>  <!-- 背景色 -->
<Color x:Key="SelectedUnfocusedColor">#FFDDDDDD</Color>   <!-- 没有焦点的颜色-->

<!-- 静态控件的颜色 -->
<Color x:Key="ControlLightColor">Transparent</Color>      <!--默认情况下是渐变色-->
<Color x:Key="ControlMediumColor">Transparent</Color>     <!-- 由这个和上一个颜色的渐变色-->
<Color x:Key="ControlDarkColor">#FF211AA9</Color>      <!-- 暂时没有用到这个 -->

<!--控件鼠标经过的颜色-->
<Color x:Key="ControlMouseOverColor">#FF3843C4</Color>
<Color x:Key="ControlPressedColor">#FF211AA9</Color>


<Color x:Key="GlyphColor">#FF444444</Color>                                        <!-- 右边倒三角箭头的填充色-->
<Color x:Key="GlyphMouseOver">sc#1, 0.004391443, 0.002428215, 0.242281124</Color>  <!-- 暂时没有用到 -->

<!--Border colors-->
<!-- 边框的颜色-->
<Color x:Key="BorderLightColor">#FFCCCCCC</Color>
<Color x:Key="BorderMediumColor">#FF888888</Color>
<Color x:Key="BorderDarkColor">#FF444444</Color>

<Color x:Key="PressedBorderLightColor">#FF888888</Color>
<Color x:Key="PressedBorderDarkColor">#FF444444</Color>

<Color x:Key="DisabledBorderLightColor">#FFAAAAAA</Color>
<Color x:Key="DisabledBorderDarkColor">#FF888888</Color>

<Color x:Key="DefaultBorderBrushDarkColor">Black</Color>



<!-- 下拉框和按钮的模板 -->
<ControlTemplate x:Key="ComboBoxToggleButton"
             TargetType="{x:Type ToggleButton}">
    <!--分成两部分，左边是文本框，右边是一个下拉按钮-->
    <Grid>
        <Grid.ColumnDefinitions>
            <ColumnDefinition />
            <ColumnDefinition Width="20" />
        </Grid.ColumnDefinitions>
        <VisualStateManager.VisualStateGroups>
            <VisualStateGroup x:Name="CommonStates">
                <VisualState x:Name="Normal" />
                <VisualState x:Name="MouseOver">
                    <Storyboard>
                        <ColorAnimationUsingKeyFrames Storyboard.TargetProperty="(Panel.Background).
            (GradientBrush.GradientStops)[1].(GradientStop.Color)"
                                      Storyboard.TargetName="Border">
                            <EasingColorKeyFrame KeyTime="0"
                               Value="{StaticResource ControlMouseOverColor}" />
                        </ColorAnimationUsingKeyFrames>
                    </Storyboard>
                </VisualState>
                <VisualState x:Name="Pressed" />
                <VisualState x:Name="Disabled">
                    <Storyboard>
                        <ColorAnimationUsingKeyFrames Storyboard.TargetProperty="(Panel.Background).
            (GradientBrush.GradientStops)[1].(GradientStop.Color)"
                                      Storyboard.TargetName="Border">
                            <EasingColorKeyFrame KeyTime="0"
                               Value="{StaticResource DisabledControlDarkColor}" />
                        </ColorAnimationUsingKeyFrames>
                        <ColorAnimationUsingKeyFrames Storyboard.TargetProperty="(Shape.Fill).
            (SolidColorBrush.Color)"
                                      Storyboard.TargetName="Arrow">
                            <EasingColorKeyFrame KeyTime="0"
                               Value="{StaticResource DisabledForegroundColor}" />
                        </ColorAnimationUsingKeyFrames>
                        <ColorAnimationUsingKeyFrames Storyboard.TargetProperty="(Border.BorderBrush).
            (GradientBrush.GradientStops)[1].(GradientStop.Color)"
                                      Storyboard.TargetName="Border">
                            <EasingColorKeyFrame KeyTime="0"
                               Value="{StaticResource DisabledBorderDarkColor}" />
                        </ColorAnimationUsingKeyFrames>
                    </Storyboard>
                </VisualState>
            </VisualStateGroup>
            <VisualStateGroup x:Name="CheckStates">
                <VisualState x:Name="Checked">
                    <Storyboard>
                        <ColorAnimationUsingKeyFrames Storyboard.TargetProperty="(Panel.Background).
            (GradientBrush.GradientStops)[1].(GradientStop.Color)"
                                      Storyboard.TargetName="Border">
                            <EasingColorKeyFrame KeyTime="0"
                               Value="{StaticResource ControlPressedColor}" />
                        </ColorAnimationUsingKeyFrames>
                    </Storyboard>
                </VisualState>
                <VisualState x:Name="Unchecked" />
                <VisualState x:Name="Indeterminate" />
            </VisualStateGroup>
        </VisualStateManager.VisualStateGroups>
        <!--横跨下拉框和按钮的边框-->
        <Border x:Name="Border"
        Grid.ColumnSpan="2"
        CornerRadius="2"
        BorderThickness="1">
            <Border.BorderBrush> <!-- 笔刷-->
                <LinearGradientBrush EndPoint="0,1"
                         StartPoint="0,0">
                    <GradientStop Color="{DynamicResource BorderLightColor}"
                    Offset="0" />
                    <GradientStop Color="{DynamicResource BorderDarkColor}"
                    Offset="1" />
                </LinearGradientBrush>
            </Border.BorderBrush>
            <Border.Background> <!--背景色-->
                <LinearGradientBrush StartPoint="0,0"
                         EndPoint="0,1">
                    <LinearGradientBrush.GradientStops>
                        <GradientStopCollection>
                            <GradientStop Color="{DynamicResource ControlLightColor}" />
                            <GradientStop Color="{DynamicResource ControlMediumColor}"
                        Offset="1.0" />
                        </GradientStopCollection>
                    </LinearGradientBrush.GradientStops>
                </LinearGradientBrush>
            </Border.Background>
        </Border>
        <!-- 左边文本输入框的框-->
        <Border Grid.Column="0"
        CornerRadius="2,0,0,2"
        Margin="1" >
            <Border.Background>
                <SolidColorBrush Color="{DynamicResource ControlLightColor}"/>
            </Border.Background>
        </Border>
        <!--右边下拉框的框-->
        <Path x:Name="Arrow"
      Grid.Column="1"
      HorizontalAlignment="Center"
      VerticalAlignment="Center"
      Data="M 0 0 L 4 4 L 8 0 Z" >
            <Path.Fill>
                <SolidColorBrush Color="{DynamicResource GlyphColor}"/>
            </Path.Fill>
        </Path>
    </Grid>
</ControlTemplate>

<!--文本输入框的外框 -->
<ControlTemplate x:Key="ComboBoxTextBox"
             TargetType="{x:Type TextBox}">
    <Border x:Name="PART_ContentHost"
      Focusable="False"
      Background="{TemplateBinding Background}" />
</ControlTemplate>

<Style x:Key="{x:Type ComboBox}"
   TargetType="{x:Type ComboBox}">
    <Setter Property="SnapsToDevicePixels"
      Value="true" />
    <Setter Property="OverridesDefaultStyle"
      Value="true" />
    <Setter Property="ScrollViewer.HorizontalScrollBarVisibility"
      Value="Auto" />
    <Setter Property="ScrollViewer.VerticalScrollBarVisibility"
      Value="Auto" />
    <Setter Property="ScrollViewer.CanContentScroll"
      Value="true" />
    <Setter Property="MinWidth"
      Value="120" />
    <Setter Property="MinHeight"
      Value="20" />
    <Setter Property="Template">
        <Setter.Value>
            <ControlTemplate TargetType="{x:Type ComboBox}">
                <Grid>
                    <VisualStateManager.VisualStateGroups>
                        <VisualStateGroup x:Name="CommonStates">
                            <VisualState x:Name="Normal" />
                            <VisualState x:Name="MouseOver" />
                            <VisualState x:Name="Disabled">
                                <Storyboard>
                                    <ColorAnimationUsingKeyFrames Storyboard.TargetName="PART_EditableTextBox"
                                            Storyboard.TargetProperty="(TextElement.Foreground).
                  (SolidColorBrush.Color)">
                                        <EasingColorKeyFrame KeyTime="0"
                                     Value="{StaticResource DisabledForegroundColor}" />
                                    </ColorAnimationUsingKeyFrames>
                                </Storyboard>
                            </VisualState>
                        </VisualStateGroup>
                        <VisualStateGroup x:Name="EditStates">
                            <VisualState x:Name="Editable">
                                <Storyboard>
                                    <ObjectAnimationUsingKeyFrames Storyboard.TargetProperty="(UIElement.Visibility)"
                                             Storyboard.TargetName="PART_EditableTextBox">
                                        <DiscreteObjectKeyFrame KeyTime="0"
                                        Value="{x:Static Visibility.Visible}" />
                                    </ObjectAnimationUsingKeyFrames>
                                    <ObjectAnimationUsingKeyFrames
                  Storyboard.TargetProperty="(UIElement.Visibility)"
                                             Storyboard.TargetName="ContentSite">
                                        <DiscreteObjectKeyFrame KeyTime="0"
                                        Value="{x:Static Visibility.Hidden}" />
                                    </ObjectAnimationUsingKeyFrames>
                                </Storyboard>
                            </VisualState>
                            <VisualState x:Name="Uneditable" />
                        </VisualStateGroup>
                    </VisualStateManager.VisualStateGroups>
                    <ToggleButton x:Name="ToggleButton"
                    Template="{StaticResource ComboBoxToggleButton}"
                    Grid.Column="2"
                    Focusable="false"
                    ClickMode="Press"
                    IsChecked="{Binding IsDropDownOpen, Mode=TwoWay, 
          RelativeSource={RelativeSource TemplatedParent}}"/>
                    <ContentPresenter x:Name="ContentSite"
                        IsHitTestVisible="False"
                        Content="{TemplateBinding SelectionBoxItem}"
                        ContentTemplate="{TemplateBinding SelectionBoxItemTemplate}"
                        ContentTemplateSelector="{TemplateBinding ItemTemplateSelector}"
                        Margin="3,3,23,3"
                        VerticalAlignment="Stretch"
                        HorizontalAlignment="Left">
                    </ContentPresenter>
                    <TextBox x:Name="PART_EditableTextBox"
               Style="{x:Null}"
               Template="{StaticResource ComboBoxTextBox}"
               HorizontalAlignment="Left"
               VerticalAlignment="Bottom"
               Margin="3,3,23,3"
               Focusable="True"
               Background="Transparent"
               Visibility="Hidden"
               IsReadOnly="{TemplateBinding IsReadOnly}" />
                    <Popup x:Name="Popup"
             Placement="Bottom"
             IsOpen="{TemplateBinding IsDropDownOpen}"
             AllowsTransparency="True"
             Focusable="False"
             PopupAnimation="Slide">
                        <Grid x:Name="DropDown"
              SnapsToDevicePixels="True"
              MinWidth="{TemplateBinding ActualWidth}"
              MaxHeight="{TemplateBinding MaxDropDownHeight}">
                            <Border x:Name="DropDownBorder"
                  BorderThickness="1">
                                <Border.BorderBrush>
                                    <SolidColorBrush Color="{DynamicResource BorderMediumColor}" />
                                </Border.BorderBrush>
                                <Border.Background>
                                    <SolidColorBrush Color="{DynamicResource ControlLightColor}" />
                                </Border.Background>
                            </Border>
                            <ScrollViewer Margin="4,6,4,6"
                        SnapsToDevicePixels="True">
                                <StackPanel IsItemsHost="True"
                        KeyboardNavigation.DirectionalNavigation="Contained" />
                            </ScrollViewer>
                        </Grid>
                    </Popup>
                </Grid>
                <ControlTemplate.Triggers>
                    <Trigger Property="HasItems"
               Value="false">
                        <Setter TargetName="DropDownBorder"
                Property="MinHeight"
                Value="95" />
                    </Trigger>
                    <Trigger Property="IsGrouping"
               Value="true">
                        <Setter Property="ScrollViewer.CanContentScroll"
                Value="false" />
                    </Trigger>
                    <Trigger SourceName="Popup"
               Property="AllowsTransparency"
               Value="true">
                        <Setter TargetName="DropDownBorder"
                Property="CornerRadius"
                Value="4" />
                        <Setter TargetName="DropDownBorder"
                Property="Margin"
                Value="0,2,0,0" />
                    </Trigger>
                </ControlTemplate.Triggers>
            </ControlTemplate>
        </Setter.Value>
    </Setter>
</Style>

<Style x:Key="{x:Type ComboBoxItem}"
   TargetType="{x:Type ComboBoxItem}">
    <Setter Property="SnapsToDevicePixels"
      Value="true" />
    <Setter Property="OverridesDefaultStyle"
      Value="true" />
    <Setter Property="Template">
        <Setter.Value>
            <ControlTemplate TargetType="{x:Type ComboBoxItem}">
                <Border x:Name="Border"
            Padding="2"
            SnapsToDevicePixels="true"
            Background="Transparent">
                    <VisualStateManager.VisualStateGroups>
                        <VisualStateGroup x:Name="SelectionStates">
                            <VisualState x:Name="Unselected" />
                            <VisualState x:Name="Selected">
                                <Storyboard>
                                    <ColorAnimationUsingKeyFrames Storyboard.TargetName="Border"
                                            Storyboard.TargetProperty="(Panel.Background).
                (SolidColorBrush.Color)">
                                        <EasingColorKeyFrame KeyTime="0"
                                     Value="{StaticResource SelectedBackgroundColor}" />
                                    </ColorAnimationUsingKeyFrames>
                                </Storyboard>
                            </VisualState>
                            <VisualState x:Name="SelectedUnfocused">
                                <Storyboard>
                                    <ColorAnimationUsingKeyFrames Storyboard.TargetName="Border"
                                            Storyboard.TargetProperty="(Panel.Background).
                (SolidColorBrush.Color)">
                                        <EasingColorKeyFrame KeyTime="0"
                                     Value="{StaticResource SelectedUnfocusedColor}" />
                                    </ColorAnimationUsingKeyFrames>
                                </Storyboard>
                            </VisualState>
                        </VisualStateGroup>
                    </VisualStateManager.VisualStateGroups>
                    <ContentPresenter />
                </Border>
            </ControlTemplate>
        </Setter.Value>
    </Setter>
</Style>


```
