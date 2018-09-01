"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------------
 @Description : 从接口中获取除了主要内容之外的数据，写入MySQL
 --------------------------------------
 @File        : downData2MySQL.py
 @Time        : 2018/4/26 16:55
 @Software    : PyCharm
 --------------------------------------
 @Author      : lixj
 @Contact     : lixj_zj@163.com
 --------------------------------------
"""

import pymysql

def write2mysql(list):
    conn = pymysql.connect(host="localhost", user='root', password='123456789', database = 'news', charset='utf8')
    cursor = conn.cursor();
    sql = "INSERT INTO docList(news_id, title, time, source, abstract) values " \
          "('%s','%s','%s','%s','%s')" % (list[0], list[1], list[2], list[3], list[4])
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

# 要求文件为utf-8类型
def cleanData(dataFilePath):
    with open(dataFilePath, "r",encoding="utf-8-sig") as f:
        allData = f.read()
        cleandData = allData.replace("||", "|")
        dataList = cleandData.split("|,")
        for oneData in dataList:
            try:
                oneDataList = oneData.split("|")
                resultDataList = [oneDataList[0], oneDataList[1], oneDataList[2], oneDataList[3], oneDataList[5]]
                write2mysql(resultDataList)
            except:
                continue

if __name__ == '__main__':
    dataFilePath = "D:/data.txt"
    cleanData(dataFilePath)


