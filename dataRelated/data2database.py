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


def write2mysql(jsonData):
    conn = pymysql.connect(host="localhost", user='root', password='123456789', database = 'ai_recommendation', charset='utf8')
    cursor = conn.cursor();
    sql = "INSERT INTO news(news_id, title, time_publish, source, abstract, content, time_create) values " \
          "('%s','%s','%s','%s','%s','%s','%s')" % \
          (jsonData.uuid, jsonData.title, jsonData.dateTime, jsonData.url, None, jsonData.content, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

if __name__ == '__main__':
    oneJsonData = dataProcessing.getOneJsonData()
    write2mysql(oneJsonData)



