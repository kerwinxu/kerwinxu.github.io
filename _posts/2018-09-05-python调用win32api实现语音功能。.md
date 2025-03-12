---
title: "python调用win32api实现语音功能。"
date: "2018-09-05"
categories: 
  - "python"
---

`#!/usr/bin/env python # -*- coding: utf-8 -*- """@File Name: speak_hello.py @Author: kerwin.cn@gmail.com @Created Time:2018-09-05 20:15:34 @Last Change: 2018-09-05 20:15:34 @Description : 这个暂时只是用win32实现语音的。 """`

import win32com.client spk = win32com.client.Dispatch("SAPI.SpVoice") spk.Speak("我是徐恒晓。") spk.Speak("I am kerwin.") spk.Speak("数字为1982")
