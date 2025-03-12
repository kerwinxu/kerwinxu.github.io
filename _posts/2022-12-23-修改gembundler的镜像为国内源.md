---
layout: post
title: "修改Gem,Bundler的镜像为国内源"
date: "2022-12-23"
categories: 
  - "ruby"
---

```
# 移除gem默认源，改成ruby-china源
$ gem sources -r https://rubygems.org/ -a https://gems.ruby-china.com/
# 使用Gemfile和Bundle的项目，可以做下面修改，就不用修改Gemfile的source
$ bundle config mirror.https://rubygems.org https://gems.ruby-china.com
# 删除Bundle的一个镜像源
$ bundle config --delete 'mirror.https://rubygems.org'
```
