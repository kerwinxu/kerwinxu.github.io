---
layout: post
title: "c#解析HTML工具 HtmlAgilityPack"
date: "2017-06-12"
categories: 
  - "c"
---

在vs2015里的Nuget中，可以搜索 HtmlAgilityPack并安装。

1. 加载html,using HtmlAgilityPack;，有2种加载方式，var doc = new HtmlAgilityPack.HtmlDocument();
    1. load(文件),
    2. loadhtml(字符串).
2. xpath:
    1. SelectSingleNode //寻找第一个节点HtmlNode
    2. SelectNode //得到的是节点集合。HtmlNodeCollection
3. 属性：GetAttributeValue，获得属性用这个，且最好用这个，在xpath中用@的方式是得不到属性的，得到的是整个节点。
4. 注意，如果在子节点中用SelectSingleNode，会以document来搜索，而不是以这个子节点来搜索，这时候得用HtmlNode.CreateNode(节点)来创建一个新的节点，然后在这个节点上SelectSingleNode，就会以这个节点搜索了。
