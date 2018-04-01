#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: e:\Program\blog\kerwinxu.github.io\auto_insert_or_update_article.py
# Project: e:\Program\blog\kerwinxu.github.io
# Created Date: Sunday, April 1st 2018, 1:33:11 pm
# Author: kerwin xu
# -----
# Last Modified:
# Modified By:
# -----
# Copyright (c) 2018 kerwin_xu
#
# 这个程序很简单，从我的wordpress上下载文章，然后更新到我的博客上的。
# 这个程序功能简单，首先从命令行得到参数，参数用来
# 我简单点，我的页面url为：http://127.0.0.1/?p=1430，程序的参数暂时为这个类似1430的数字吧。
# 然后下载文章，取得相关标签内的数据,然后在本地新建一个或者打开一个文件，文件名暂时是这个标题的拼音吧。
# 实现步骤如下
# getopt来当取得命令行参数的，用-n 参数来表示这个页面的数字吧，以后加上搜索功能。
# python下载，
# 文章主体在：<div class="entry-content clearfixafter"> 中
# 文章标题在：<header class="entry-header">		<h1 itemprop="headline" title="支持向量机" class="entry-title">支持向量机</h1>
#       <span itemprop="image" itemscope="" itemtype="https://schema.org/ImageObject"><meta itemprop="url" content="http://127.0.0.1/wp-content/themes/zoom-lite/assets/images/misc/placeholder/thumb-medium.png"><meta itemprop="width" content="569"><meta itemprop="height" content="309"></span>		<div class="entry-meta">
#			<i class="fa fa-calendar zoom-meta-date-posted" aria-hidden="true"></i>Posted on <a href="http://127.0.0.1/?p=1430" title="下午10:45" rel="bookmark"><time itemprop="datePublished" class="entry-date" datetime="2018-03-14T22:45:51+00:00" pubdate="">三月 14, 2018</time></a><span class="byline"> by <span class="author vcard"><a class="url fn n" href="http://127.0.0.1/?author=1" title="View all posts by xuhengxiao" rel="author">xuhengxiao</a></span></span>		</div><!-- .entry-meta -->
#	</header>
# 但其实只要这部分就可以了。 <h1 itemprop="headline" title="支持向量机" class="entry-title">支持向量机</h1>
# 关于要上传到github上的html文件，需要修改的2个部分
# 一个是文章页面
#       文章页面有3部分,分别是头和尾，再加上body，也就是文章的具体内容啦。
#
# 一个是index.html页面。
###

import getopt
import sys
import os
import logging
import urllib.request
from lxml import etree
from pypinyin import pinyin, lazy_pinyin, Style
logging.basicConfig(level=logging.DEBUG)

# 文章的页面头部
HTML_HEAD = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>矩阵向量求导方法 &#8211; 徐恒晓学习</title>
<script type="text/javascript" charset="utf-8" src="
https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML,
https://kerwinxu.github.io/MathJaxLocal.js"></script>
</head>
<body> '''
# 文章的页面尾部
HTML_END = """</body></html>"""


def main():
    """ main 函数
    """
    # 这里是程序运行的地方。
    # 首先读取命令行参数啦。
    page_number = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:h")
    except getopt.GetoptError as err:
        logging.error("err{}".format(err))
        sys.exit()
    for opt, arg in opts:
        if opt == '-n':
            page_number = int(arg)
            logging.info("输入页面ID为{}".format(page_number))
    # 然后就是组建字符串啦。
    # 首先判断有没有找到这个页面
    if page_number is None:
        logging.error("没有页面ID")
        sys.exit()
    article_url_local = "http://127.0.0.1/?p={}".format(page_number)
    # 然后就是下载啦
    # 我自己的页面，utf-8，省略判断编码了
    # 用一个超长的来表示吧。简单点
    article_html = urllib.request.urlopen(
        article_url_local).read().decode('utf-8')
    # 这里需要寻找2个遍历，一个是文章标题，一个是文章内容。
    tree = etree.HTML(article_html)
    article_title = tree.xpath('//h1[@itemprop="headline"]/@title')
    if len(article_title) > 0:
        article_title = article_title[0]
        logging.info("获得文章标题:{}".format(article_title))
    else:
        logging.error("不能获得文章标题")
        sys.exit()
    # 然后获得文章内容
    article_body = tree.xpath('//div[@class="entry-content clearfixafter"]')
    if len(article_body) > 0:
        article_body = (etree.tostring(article_body[0])).decode('utf-8')
        logging.info("获得的文章字节数为:{}".format(len(article_body)))
    else:
        logging.error("不能获得文章内容")
        sys.exit()

    # 生成文件名，根据拼音。
    file_name = ''.join(lazy_pinyin(article_title)) + ".html"
    # 判断文件是否存在。
    # 首先组建路径啦。
    _dir = os.path.dirname(__file__)
    file_path = os.path.join(_dir, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
    # 然后打开文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(HTML_HEAD)      # 头部
        f.write(article_body)   # 文章内容
        f.write(HTML_END)  # 尾部
    # 然后是修改主页啦。
    # 首先也是读入
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    etree_index = etree.HTML(open(index_path, encoding='utf-8').read())
    # 首先查找域名
    # 这个网站的url是类似这种  "./martixdiff.html"
    article_url_remote = "./{}".format(file_name)
    article_url_remote_in_index = etree_index.xpath(
        '//li[contains(a,"{}")]'.format(article_url_remote))
    if(len(article_url_remote_in_index) > 0):
        logging.info("原先就有这个网址,不用做操作")
        sys.exit()
    # 到这里就表示得添加新的一项了。
    _ul = etree_index.xpath("//ul")
    if(len(_ul) == 0):
        logging.error("找不到ul标签")
        sys.exit()
    # 我这里也是做省事，只是选择第一个
    _ul = _ul[0]
    _new_li = etree.Element("li")
    _new_a = etree.Element("a", href=article_url_remote,)
    _new_a.text = article_title
    _new_li.insert(0, _new_a)
    _ul.insert(0, _new_li)
    # 保存到文件啦。
    with open(index_path, 'wb') as f:
        # 我直接创建一个字符串，然后保存到文件吧。
        str_html = etree.tostring(
            etree_index, encoding='utf-8', pretty_print=True)
        f.write(str_html)


if __name__ == '__main__':
    main()
