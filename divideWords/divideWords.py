"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------------
 @Description : HanLP, baiduNLP, jieba分词对比
 百度：
    分词
    文章标签
    文章分类
hanlp：
    分词
    篇章理解
        关键词提取
        自动摘要
    智能推荐
jieba:
    分词-并提取top N 的词
    添加自定义词典
    关键词提取
 --------------------------------------
 @File    	  : divideWords.py
 @Time    	  : 2018/8/31 22:30
 @Software	  : PyCharm
 --------------------------------------
 @Author      : lixj
 @Contact     : lixj_zj@163.com
 --------------------------------------
"""

import pyhanlp
from aip import AipNlp
import jieba
import jieba.analyse
from collections import Counter
jieba.load_userdict("./userDict.txt")   # 添加自定义字典，位于import jieba下面

class hanlp:
    pass

class jieba_nlp:
    def __init__(self, text):
        self.text = text

    # 采用默认精确模式
    def cut2words(self):
        # 开启并行分词，pool_num = 4
        # jieba.enable_parallel(4)
        cutWordsResult = jieba.cut(self.text, cut_all=False)
        # jieba.disable_parallel()
        # 获取出现频率top N = 20 的词
        wordsListTopN = Counter(list(cutWordsResult)).most_common(20)
        return wordsListTopN

    def extractKeyWords_TFIDF(self):
        keyWords = jieba.analyse.extract_tags(self.text, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
        keyWords_TFIDF = [keyWord[0] for keyWord in keyWords]
        return keyWords_TFIDF

    def extractKeyWords_Textrank(self):
        keyWords_textrank = jieba.analyse.textrank(self.text, topK=20, withWeight=False, allowPOS=('ns', 'n', 'nr'))
        return keyWords_textrank

class baidu_nlp:
    def __init__(self, title, text):
        self.APP_ID = ""
        self.API_KEY = ""
        self.SECRET_KEY = ""
        self.client = AipNlp(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        self.title = title
        self.text = text

    def cut2words(self):
        cutWordsResult = self.client.lexerCustom(self.text)
        items = cutWordsResult["items"]
        # 筛选词性为名词
        nounItemList = [item["item"] for item in items if item["pos"] in ('ns', 'n', 'nr')]
        wordsListTopN = Counter(nounItemList).most_common(20)
        return wordsListTopN

    def lableOfArticles(self):
        articleLable = self.client.keyword(self.title, self.text)
        return articleLable

    def classifyArticles(self):
        classify = self.client.topic(self.title, self.text)
        return classify

if __name__ == '__main__':
    title = "9月将实施这些新规 涉及车辆 出入境等多5大方面"
    text = "开车的朋友们，9月更省事了。公安部20项交管改革新举措9月1号起全面推行。"


    # jieba_nlp = jieba_nlp(text)
    # print(jieba_nlp.cut2words())
    # print(jieba_nlp.extractKeyWords_TFIDF())
    # print(jieba_nlp.extractKeyWords_Textrank())

    # baidu_nlp = baidu_nlp(title, text)
    # baidu_nlp.cut2words()
    # baidu_nlp.lableOfArticles()
    # baidu_nlp.classifyArticles()




