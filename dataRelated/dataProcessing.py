"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------------
 @Description : General operations related to data processing
 0. 频繁的IO操作--优化方法
 1. \n 替换为空
 2. 无abstract则置空
 3. 标题截取"-"后的内容
 4. 上一页之后的切除
 --------------------------------------
 @File        : dataProcessing.py
 @Time        : 2018/9/2 21:42
 @Software    : PyCharm
 --------------------------------------
 @Author      : lixj
 @Contact     : lixj_zj@163.com
 --------------------------------------
"""

import os
import json
import datetime

# 针对特定格式的json文件
with open("../test/news_0000001.json", 'r', encoding="utf-8") as f:
    text = json.load(f)     # 处理json文件，load(f)

    # print(text["uuid"])
    # print(text["url"])
    # print(text["title"])


    content = text['text']



    # timestring = text["published"].split(".")[0].replace("T", " ")
    # string to datetime
    # dateTime = datetime.datetime.strptime(timestring, "%Y-%m-%d %H:%M:%S")
    # print(dateTime)




