---
layout: post
title: "git添加已存在工程到github远程版本库"
date: "2017-10-31"
categories: ["构建"]
---

首先，在github上建立远程版本库https://github.com/mygit/testgit.git

将本地工程添加到远程版本库中去

\[plain\] view plaincopyprint?

git init                                        //  初始化git环境

git config --global user.name 'name'            //  配置用户名，以便于远程提交

git config --global user.email xxx@xxx.xxx      //  配置用户邮箱，以便于远程提交

git add .                                       //  添加所有文件

git commit -m 'commit'                          //  提交到本地库

git remote add nickname https://github.com/yourgit/testgit.git  //  添加远程版本库

git push nickname master                        //  将本地master分支提交到远程分支

git remote show nickname                        //  显示远程信息

如果出现”Updates were rejected because the tip of your current branch is behind“错误，则说明github上的readme与本地版本冲突，可以执行如下语句强行提交

\[plain\] view plaincopyprint?

git push -u nickname master -f

从git上获取最新版本代码的命令为

\[plain\] view plaincopyprint?

git clone -b branchname username@https://github.com/yourgit/testgit.git
