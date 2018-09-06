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

import json
import datetime

class jsonData:
    def __init__(self, uuid, url, title, content, dateTime):
        self.uuid = uuid
        self.url = url
        self.title = title
        self.content = content
        self.dateTime = dateTime

    def jsonDataList(self):
        jsonDataList = [self.uuid, self.title, self.dateTime, self.url, None, self.content, self.dateTime]
        return jsonDataList

# 针对特定格式的json文件
def getOneJsonData():
    with open("../test/news_0000003.json", 'r', encoding="utf-8") as f:
        text = json.load(f)     # 处理json文件，load(f)

        originalTitle = text["title"]
        title = originalTitle.split("-")[0]

        originalContent = text['text']
        content = originalContent[:originalContent.find("上一页")].replace("\n\n", "。").replace("\n", "").replace(" ", "")

        originalTime = text["published"].split(".")[0].replace("T", " ")
        # string to datetime
        dateTime = datetime.datetime.strptime(originalTime, "%Y-%m-%d %H:%M:%S")

        oneJsonData = jsonData(text["uuid"], text["url"], title, content, dateTime)
        return oneJsonData

if __name__ == '__main__':
    oneJsonData = getOneJsonData()
    # print(oneJsonData.title)

