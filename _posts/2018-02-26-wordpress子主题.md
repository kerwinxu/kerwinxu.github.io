---
title: "wordpress子主题"
date: "2018-02-26"
categories: 
  - "wordpress相关"
---

子主题也是主题，相当于子类，继承了父类的功能，也可以修改父类的功能。

在主题目录新建一个文件夹，当子主题目录，

- **public\_html**
    - **wp-content**
        - **themes** (主题存放的目录)
            - **twentyten** (示例中父主题Twenty Ten的目录)
            - **twentyten-child** (子主题存放的目录，可以任意命名)
                - **style.css** (子主题中不可或缺的文件，文件名必需为 style.css)

这个文件夹里面可以少至只包含一个style.css文件，也可以包含多至一个完整WordPress主题所拥有的文件：

- style.css (必需)
- functions.php (可选)
- Template files (可选)
- Other files (可选)

下边是style.css头部示例

```
/*
Theme Name:     Twenty Ten Child
Theme URI:      http: //example.com/
Description:    Child theme for the Twenty Ten theme
Author:         Your name here
Author URI:     http: //example.com/about/
Template:       twentyten
Version:        0.1.0
*/
```

逐行的简单解释：

- `Theme Name`. (**必需**) 子主题的**名称**。
- `Theme URI`. (可选) 子主题的主页。
- `Description`. (可选) 子主题的描述。比如：我的第一个子主题，真棒！
- `Author URI`. (可选) 作者主页。
- `Author`. (optional) 作者的名字。
- `Template`. (**必需**) 父主题的目录名，区别大小写。 **注意：** 当你更改子主题名字时，要先换成别的主题。
- `Version`. (可选) 子主题的版本。比如：0.1，1.0，等。

`*/` 这个关闭标记的后面部分，就会按照一个常规的样式表文件一样生效，你可以把你想对WordPress应用的样式规则都写在它的后面。

要注意的是，子主题的样式表会替换父主题的样式表而生效。（事实上WordPress根本就不会载入父主题的样式表。）所以，如果你想简单地改变父主题中的一些样式和结构——而不是从头开始制作新主题——你必须明确的导入父主题的样式表，然后对它进行修改。

下面的例子告诉你如何使用`@import`规则完成这个。

### 一个子主题的范例

这个例子中的父主题是Twenty Ten，我们喜欢这个主题的几乎每个部分，除了网站标题的颜色，因为我想把它从黑色的改成绿色的。使用子主题的话，只用完成以下三个简单的步骤：

1. 在_wp-content/themes_目录下创建一个新目录，并将它命名为twentyten-child（或其他你喜欢的名称）。
2. 将下面的代码保存在名为_style.css_的文件里，并将它放到新建的这个文件夹。
3. 到WordPress的控制台>主题，然后激活你的新主题：Twenty Ten Child。

<table><tbody><tr><td class="line_numbers"><pre>1
2
3
4
5
6
7
8
9
10
11
12
</pre></td><td class="code"><pre class="css">/*
Theme Name: Twenty Ten Child
Description: Child theme for the Twenty Ten theme
Author: Your name here
Template: twentyten
*/
&nbsp;
@import url("../twentyten/style.css");
&nbsp;
#site-title a {
    color: #009900;
}</pre></td></tr></tbody></table>

下面一步步解释上面代码的作用：

1. `/*` 开启子主题的头部信息。
2. `Theme Name:` 子主题名称的声明。
3. `Description:` 主题的描述（可选，也可被省略）。
4. `Author:` 作者名字的声明（可选，也可被省略）。
5. `Template:` 声明子主题的父主题，换言之，父主题所在的文件夹的名称，区分大小写。
6. `*/`子主题头部信息的关闭标记。
7. 用 `@import`规则将父主题的样式表调入
8. `#site-title a` 定义网站标题的颜色（绿色），覆盖父主题中相同的样式规则。

#### 注意 `@import` 规则

需要注意的是，`@import` 规则之前没有其他的CSS样式规则，如果你将其他的规则置于它之上，那么它将无效，并且父主题的样式表不会被导入。

### 使用 functions.php

不像_style.css_，子主题中的_functions.php_不会覆盖父主题中对应功能，而是将新的功能加入到父主题的_functions.php_中。（其实它会在**父主题文件加载之前先载入**。）

这样，子主题的_functions.php_提供了一个灵活稳定的方式来修改父主题的功能。如果你想在你的主题里加入一些PHP函数，最快的方式可能是打开_functions.php_文件然后加入进去。但那样并不灵活：下次你的主题升级更新了，你加入的新功能就会丢失掉。相反地，如果你使用子主题，将_functions.php_文件放进去，再将你想加入的功能写进这个文件里，那么这个功能同样会工作得很好，并且对于父主题以后的升级更新，子主题中加入的功能也不会受到影响。

_functions.php_文件的结构非常简单：将PHP起始标签置于顶部，关闭标签置于底部，它们之间就写上你自己的PHP函数。你可以写得很多，也可以写得很少，反正按你所需。下面的示例是一个基本的_functions.php_文件的写法，作用是将favicon链接加入到HTML页面的head元素里面。

<table><tbody><tr><td class="line_numbers"><pre>1
2
3
4
5
6
7
8
</pre></td><td class="code"><pre class="php">&lt;?php
&nbsp;
function favicon_link() {
    echo '&lt;link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" /&gt;' . "n";
}
add_action('wp_head', 'favicon_link');
&nbsp;
?&gt;</pre></td></tr></tbody></table>

给主题作者的提示。事实上子主题的_functions.php_首先加载意味着你的主题的用户功能可插入——即子主题是可替换的——通过有条件地进行声明。例如：

<table><tbody><tr><td class="line_numbers"><pre>1
2
3
4
5
</pre></td><td class="code"><pre class="php">if (!function_exists('theme_special_nav')) {
    function theme_special_nav() {
        //  Do something.
    }
}</pre></td></tr></tbody></table>

用这种方式，子主题可以替换父主题中的一个PHP函数，只需要简单地对它再次声明。

### 模板文件

[模板文件](http://codex.wordpress.org/Templates) 在子主题中的表现和_style.css_一样，它们会**覆盖**父主题中的相同文件。子主题可以覆盖**任何**父主题模板中的文件，只需要创建同名文件就行。（注意：_index.php_在WordPress3.0及以上版本才能被覆盖。）

同样，这项WordPress的功能允许你修改父主题的样式功能而不用去编辑父主题的文件，并且你的修改能让你在更新父主题后继续保留。

下面是一些使用模板文件的子主题的例子：

- 增加一个父主题没有提供的模板（例如：网站地图页面的模板，或者一单栏页面，它们在页面编辑，模板选择里是可用的）

- 增加一个比父模板更加具体的模板（见[模板级别](http://codex.wordpress.org/Template_Hierarchy)）。（例如：新加的_tag.php_模板用于按tag归档的文章来代替父主题中通常的_archive.php_模板。）

- 替换父主题中的一个模板.（例：使用你自己的_home.php_来覆盖父主题中的_home.php_）

### 其他文件

除了style.css，functions.php，index.php和home.php，子主题可以使用任何正式主题使用的类型的文件，只要文件被正确链接。打个比方，你可以使用在样式表里或者Javascript文件里链接的图标、图片，或者从functions.php文件中调用出来的额外PHP文件。
