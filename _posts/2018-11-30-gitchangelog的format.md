---
layout: post
title: "gitchangelog的format"
date: "2018-11-30"
categories: 
  - "python"
---

```
git 的log日志规范的，这个可以方便的生成易读的log。


# -*- coding: utf-8; mode: python -*-
##
## Format
##
##   ACTION: [AUDIENCE:] COMMIT_MSG [!TAG ...]
##
## Description
##
##   ACTION is one of 'chg', 'fix', 'new'
##
##       Is WHAT the change is about.
##
##       'chg' is for refactor, small improvement, cosmetic changes...
##       'fix' is for bug fixes
##       'new' is for new features, big improvement
##
##   AUDIENCE is optional and one of 'dev', 'usr', 'pkg', 'test', 'doc'
##
##       Is WHO is concerned by the change.
##
##       'dev'  is for developpers (API changes, refactors...)
##       'usr'  is for final users (UI changes)
##       'pkg'  is for packagers   (packaging changes)
##       'test' is for testers     (test only related changes)
##       'doc'  is for doc guys    (doc only changes)
##
##   COMMIT_MSG is ... well ... the commit message itself.
##
##   TAGs are additionnal adjective as 'refactor' 'minor' 'cosmetic'
##
##       They are preceded with a '!' or a '@' (prefer the former, as the
##       latter is wrongly interpreted in github.) Commonly used tags are:
##
##       'refactor' is obviously for refactoring code only
##       'minor' is for a very meaningless change (a typo, adding a comment)
##       'cosmetic' is for cosmetic driven change (re-indentation, 80-col...)
##       'wip' is for partial functionality but complete subfunctionality.
##
## Example:
##
##   new: usr: support of bazaar implemented
##   chg: re-indentend some lines !cosmetic
##   new: dev: updated code to be compatible with last version of killer lib.
##   fix: pkg: updated year of licence coverage.
##   new: test: added a bunch of test around user usability of feature X.
##   fix: typo in spelling my name in comment. !minor
##
##   Please note that multi-line commit message are supported, and only the
##   first line will be considered as the "summary" of the commit message. So
##   tags, and other rules only applies to the summary.  The body of the commit
##   message will be displayed in the changelog without reformatting.

## 如上是最基本的。
```
