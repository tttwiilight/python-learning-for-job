#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:16:32 2026

@author: llll
"""

print("BMI计算器:D")
x=float(input("请输入您的身高(m):"))
y=float(input("请输入您的体重(kg):"))
a=y/x**2
if a<18.5:
    print(f"您的BMI是{a:.2f},属于偏瘦范围，猫粮大口吃！")
elif a>=18.5 and a<24:
      print(f"您的BMI是{a:.2f}，属于正常范围，保持就好了呀喵呜")  
elif a>=24 and a<28:
      print(f"您的BMI是{a:.2f}，属于超重范围，每次嚼几粒猫粮吧嗷")   
else:
     print(f"您的BMI是{a:.2f}，属于肥胖范围，少吃点吧( ；´Д｀)")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
