#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 14:52
# @Author  : Brawenlu
# @File    : Jd.py
# @Software: PyCharm
import logging
import requests
import lxml.html
import time
import random
import json
etree = lxml.html.etree
# import sys
# reload(sys)
# sys.setdefaultencoding('gbk')

class Jdprice(object):
    def __init__(self):
        self.host = 'https://msitepp-fm.jd.com'
        self.header={}
        self.cookie={}
        self.n=0
        # 创建一个logger
        self.logger = logging.getLogger('mylogger')
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.handler = logging.FileHandler('test.log', encoding='utf-8')
        self.handler.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        self.commandhandler = logging.StreamHandler()
        self.commandhandler.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.commandhandler.setFormatter(self.formatter)
        # 给logger添加handler
        self.logger.addHandler(self.handler)
        self.logger.addHandler(self.commandhandler)

    def priceskusPull(self):
        #获取数据
        priceurl = self.host + '/rest/priceprophone/priceskusPull'
        pricedata = {'page':'1','pageSize':'30','keyWords':'','sid':'','type':3}
        html = requests.post(url=priceurl,data=pricedata,cookies=self.cookie,headers=self.header,verify=False).content
        # print(html.decode())
        # html_res = html.encode('raw_unicode_e?scape')
        # self.logger.info(html.decode('utf-8'))
        infolist = etree.HTML(html.decode('utf-8'),etree.HTMLParser()).xpath('//a[@clstag="pageclick|keycount|M_proprice_201801099|1"]/@onclick')
        # print(infolist) 调试元素定位后的列表里面有3个值
        dict1 = {}
        for i in range(len(infolist)):
            # 把所有匹配的值放到列表里面，列表再遍历3个，从第一个下标开始，将元素分别放入dict1里面
            skuapply = str(infolist[i]).split(',')
            dict1['orderId'] = skuapply[0][9:] #取得skuapply第一个下标的值以及第10个下标开始的id
            dict1['orderCategory']='3'
            dict1['skuId']=skuapply[1]
            dict1['sid']=''
            dict1['type']=skuapply[3]
            dict1['refundtype']=skuapply[2]
            time.sleep(int(random.randint(2,8)))
            # 申请报价，调用下面的请求,参数是字典
            self.skuProtectApply(dict1)
            self.n +=1#累积报价数量
            self.logger.info(u'************************报价数量为：%s***************************'% str(self.n))

    def skuProtectApply(self,data):
        self.header.update({'content-type':'application/x-www-form-urlencoded',
                            'accept':'application/json',})
        applyurl = self.host + '//rest/priceprophone/skuProtectApply'
        resapply = requests.post(url=applyurl,data=data,cookies=self.cookie,verify=False,headers=self.header)
        # print(type(resapply))
        self.logger.info(json.dumps(resapply.json(),indent=2,sort_keys=True,ensure_ascii=False)) #indent代表缩进，sort_keys代表是否键值升序，ensure__ascil要中文正常显示（默认是ascil编码）

if __name__=='__main__':
    luwenbo = Jdprice()
    luwenbo.priceskusPull()

