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
import gevent
from dataRelated import dataProcessing
import traceback

class data2Mysql:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "123456789"
        self.database = "ai_recommendation"
        self.charset = "utf8"

    def DBConnect(self):
        self.conn = pymysql.connect(host = self.host, user = self.user, password = self.password, database = self.database, charset = self.charset)
        self.cursor = self.conn.cursor();

    # 异步插入数据
    def asynchronous(self, maxLineInsert, totalDataVolume, jsonData):
        taskList = [gevent.spawn(self.write2mysql(i, i+maxLineInsert, jsonData)) for i in range(1, totalDataVolume, maxLineInsert)]
        gevent.joinall(taskList)
        self.cursor.close()
        self.conn.close()

    def write2mysql(self, nmin, nmax, jsonData):
        list = []
        for i in range(nmin, nmax):
            list.append((jsonData.uuid, jsonData.title, jsonData.dateTime, jsonData.url, None,
                         jsonData.content, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

        sql = "INSERT INTO news(news_id, title, time_publish, source, abstract, content, time_create) values " \
              "(%s, %s, %s, %s, %s, %s, %s)"
        try:
            affectedRows = self.cursor.executemany(sql, list)
            # 打印输出依然耗时
            # if affectedRows:
            #     print("已完成：", affectedRows, "行.")
            self.conn.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()

# jsonData 作为参数传递的次数越少越好
if __name__ == '__main__':
    oneJsonData = dataProcessing.getOneJsonData()

    # 每次最大插入行数
    maxLineInsert = 100
    # 插入数据总数
    totalDataVolume = 1000

    beginTime = time.time()
    data2Mysql = data2Mysql()
    data2Mysql.DBConnect()
    data2Mysql.asynchronous(maxLineInsert, totalDataVolume, oneJsonData)
    print("used time:", (time.time()-beginTime))
