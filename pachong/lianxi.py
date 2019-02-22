#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 16:15
# @Author  : Brawenlu
# @File    : lianxi.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import lxml.html,requests,sys,time,random,json
etree = lxml.html.etree


list = ["skuApply(87057118606,100001324350,1,3,'Others')", "skuApply(83098583737,6528331,1,3,'Others')", "skuApply(85108703149,6233877,1,3,'Others')"]
for i in range(len(list)):
    res = str(list[i]).split(',')
    print(str(list[i]))
    res1 = res[0].split('(')
    print(res1[1])
    print(res[0][9:])


# print(time.sleep(int(random.randint(2,4))))
# self=0
# self+=2
# print('报价数量为：%s'% str(self))
res = {"proApplyId":-100,"flag":'true',"errorCode":"0","errorMessage":"","proSkuApplyId":[100055617]}
print(json.dumps(res,indent=2,sort_keys=True,ensure_ascii=False))
