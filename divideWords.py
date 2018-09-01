# """
#  !/usr/bin/env python3.6
#  -*- coding: utf-8 -*-
#  --------------------------------------
#  @Description : HanLP, baiduNLP, jieba分词对比
#  百度：
#     分词
#     依存句法分析
#     评论观点抽取
#     文章标签
#     文章分类
# hanlp：
#     分词
#     篇章理解
#         关键词提取
#         自动摘要
#     智能推荐
# jieba:
#     分词
#     添加自定义词典
#     关键词提取
#  --------------------------------------
#  @File    	  : divideWords.py
#  @Time    	  : 2018/8/31 22:30
#  @Software	  : PyCharm
#  --------------------------------------
#  @Author      : lixj
#  @Contact     : lixj_zj@163.com
#  --------------------------------------
# """
#
from pyhanlp import *
from aip import AipNlp
import jieba
import jieba.analyse

class baidu_nlp:
    def __init__(self):
        self.APP_ID = "020e0df2b55441d9b90861ea2b457ddf"
        self.API_KEY = "51fa55f6feb94a0fb7d4de49f111d6c2"
        self.SECRET_KEY = "129ba31afdaa439da5cf9ab0cd07d8f4"
        self.client = AipNlp(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def cifa(self, text):
        cifa = self.client.lexer(text)
        print(cifa)

class jieba:
    def __init__(self, text):
        self.text = text

    def divideWord(self):
        # result = jieba.cut(self.text, cut_all=True)
        keywords = jieba.analyse.extract_tags(self.text, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
        print(keywords)

class hanlp:
    pass

if __name__ == '__main__':
    text = "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。"
    # baidu_nlp = baidu_nlp()
    # baidu_nlp.cifa(text)

    jb = jieba(text)
    jb.divideWord()


# print(HanLP.segment("你好，欢迎在Python中调用HanLP的API"))
#
# testCase = [
# "商品和服务",
# "结婚的和尚未结婚的确实在干扰分词啊",
# "买水果然后来世博园最后去世博会",
# "中国的首都是北京",
# "欢迎新老师生前来就餐",
# "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
# "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。"]
# for sentence in testCase:
# print(HanLP.segment(sentence))

# encoding=utf-8
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))




import jieba
import jieba.analyse

sentence = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"

keywords = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n','nr','ns'))

# print(type(keywords))
# <class 'list'>

for item in keywords:
    print(item[0],item[1])