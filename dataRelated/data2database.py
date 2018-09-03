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

from dataRelated import dataProcessing

oneJsonData = dataProcessing.getOneJsonData()


