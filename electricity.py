#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:19:25 2026

@author: llll
"""

ele=int(input("输入用电度数："))
if ele<2880:
    print("电费价格为：",ele*0.4883)
elif ele>=2880 and ele<=4800:
      print("电费价格为",2880*0.4883+(ele-2880)*0.5383)
else:
    print("电费价格为：",2880*0.4883+1920*0.5383+(ele-4800)*0.7883)