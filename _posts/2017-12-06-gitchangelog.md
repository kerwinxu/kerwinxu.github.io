---
layout: post
title: "gitchangelog -> 将git log变成更美观的输出"
date: "2017-12-06"
categories: 
  - "git"
  - "python"
---

这个只是用来将git log变成更美观的输出，安装是pip install gitchangelog

简单将，版本号是git tag 来生成的

而在git commit -m 中，要遵循如下的编写

ACTION: \[AUDIENCE:\] COMMIT\_MSG \[!TAG ...\]

1. ACTION是 'chg', 'fix', 'new'
    1. \## 'chg' is for refactor, small improvement, cosmetic changes... 小修改
    2. \## 'fix' is for bug fixes 修复补丁
    3. \## 'new' is for new features, big improvement 大修改
2. AUDIENCE is optional and one of 'dev', 'usr', 'pkg', 'test', 'doc'
    1. \## 'dev' is for developpers (API changes, refactors...) API修改，重构
    2. \## 'usr' is for final users (UI changes) 界面修改
    3. \## 'pkg' is for packagers (packaging changes) 打包方式更改
    4. \## 'test' is for testers (test only related changes) 测试相关的改变
    5. \## 'doc' is for doc guys (doc only changes) 文档相关的改变

\# -\*- coding: utf-8; mode: python -\*- ## ## Format ## ## ACTION: \[AUDIENCE:\] COMMIT\_MSG \[!TAG ...\] ## ## Description ## ## ACTION is one of 'chg', 'fix', 'new' ## ## Is WHAT the change is about. ## ## 'chg' is for refactor, small improvement, cosmetic changes... ## 'fix' is for bug fixes ## 'new' is for new features, big improvement ## ## AUDIENCE is optional and one of 'dev', 'usr', 'pkg', 'test', 'doc' ## ## Is WHO is concerned by the change. ## ## 'dev' is for developpers (API changes, refactors...) ## 'usr' is for final users (UI changes) ## 'pkg' is for packagers (packaging changes) ## 'test' is for testers (test only related changes) ## 'doc' is for doc guys (doc only changes) ## ## COMMIT\_MSG is ... well ... the commit message itself. ## ## TAGs are additionnal adjective as 'refactor' 'minor' 'cosmetic' ## ## They are preceded with a '!' or a '@' (prefer the former, as the ## latter is wrongly interpreted in github.) Commonly used tags are: ## ## 'refactor' is obviously for refactoring code only ## 'minor' is for a very meaningless change (a typo, adding a comment) ## 'cosmetic' is for cosmetic driven change (re-indentation, 80-col...) ## 'wip' is for partial functionality but complete subfunctionality. ## ## Example: ## ## new: usr: support of bazaar implemented ## chg: re-indentend some lines !cosmetic ## new: dev: updated code to be compatible with last version of killer lib. ## fix: pkg: updated year of licence coverage. ## new: test: added a bunch of test around user usability of feature X. ## fix: typo in spelling my name in comment. !minor ## ## Please note that multi-line commit message are supported, and only the ## first line will be considered as the "summary" of the commit message. So ## tags, and other rules only applies to the summary. The body of the commit ## message will be displayed in the changelog without reformatting.
