"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------------
 @Description : Store the processed data in the database
 --------------------------------------
 @File        : data2database.py
 @Time        : 2018/9/2 21:46
 @Software    : PyCharm
 --------------------------------------
 @Author      : lixj
 @Contact     : lixj_zj@163.com
 --------------------------------------
"""

import pymysql
import time
from dataRelated import dataProcessing
import traceback

class pymysql:
    def __init__(self):
        pass

def write2mysql(jsonData):
    conn = pymysql.connect(host="localhost", user='root', password='123456789', database = 'ai_recommendation', charset='utf8')
    cursor = conn.cursor();

    list = []
    for i in range(200):
        list.append((jsonData.uuid, jsonData.title, jsonData.dateTime, jsonData.url, None,
                     jsonData.content, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    sql = "INSERT INTO news(news_id, title, time_publish, source, abstract, content, time_create) values " \
          "(%s, %s, %s, %s, %s, %s, %s)"
    print(sql)
    try:
        affectedRows = cursor.executemany(sql, list)
        if affectedRows:
            print("已完成：", affectedRows, "行.")
        conn.commit()
    except:
        print(traceback.format_exc())
        conn.rollback()

if __name__ == '__main__':
    oneJsonData = dataProcessing.getOneJsonData()
    beginTime = time.time()
    write2mysql(oneJsonData)
    print("used time:", (time.time()-beginTime))


