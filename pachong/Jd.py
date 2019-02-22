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
        self.header={'user-agent':'jdapp;iPhone;7.3.6;12.1.2;5123eb25ec6f51da6cd30ebd9ed0fa3c7e6746a2;network/wifi;ADID/19884735-635B-4056-B10F-745E89C334DE;supportApplePay/3;hasUPPay/0;pushNoticeIsOpen/0;model/iPhone8,1;addressid/643744556;hasOCPay/0;appBuild/164946;supportBestPay/0;pv/240.15;pap/JA2015_311210|7.3.6|IOS 12.1.2;apprpd/MyJD_Main;psn/5123eb25ec6f51da6cd30ebd9ed0fa3c7e6746a2|539;usc/toutiao_video;jdv/0|toutiao_video|t_1000067282_318559470_3942|adrealizable|_2_app_0_50c720ad67d74a63a15fca5f96fb427d-p_3942|1544611321;umd/adrealizable;psq/1;ucp/t_1000067282_318559470_3942;app_device/IOS;adk/;ref/MyJdMTAManager;utr/_2_app_0_50c720ad67d74a63a15fca5f96fb427d-p_3942;ads/;Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16C101;supportJDSHWK/1'}
        self.cookie={'__jda':'206979520.15193562587261973407271.1519356258.1550629087.1550634338.162',
                     '__jdb':'206979520.2.15193562587261973407271|162.1550634338',
                     '__jdc':'206979520',
                     '__jdv':'206979520|toutiao_video|t_1000067282_318559470_3942|adrealizable|_2_app_0_50c720ad67d74a63a15fca5f96fb427d-p_3942|1544611321000',
                     'mba_muid':'15193562587261973407271.240.1550634343390',
                     'mba_sid':'240.17',
                     'pre_seq':'1',
                     'pre_session':'5123eb25ec6f51da6cd30ebd9ed0fa3c7e6746a2|539',
                     'priceProPin':'ZYGWXO2N45EKUC2JOYM52TBTNE',
                     'pt_key':'app_openAAFcbLjeADDkDsR0lQXe-ClVhOzu6v1E2gNyv-9CB2v-aMSz7kEs1CqAzkMFxeh7EAOWSY6_2_0',
                     'pt_pin':'%E5%BF%83%E5%8F%AA%E4%B8%BA%E5%8D%9A',
                     'pwdt_id':'%E5%BF%83%E5%8F%AA%E4%B8%BA%E5%8D%9A',
                     'sid':'d729db2caa3d71df7b57b7c9174c476w',
                     'unpl':'ADC_7H5VQQVKoCs%2FK8Uw27Df5zyD7cGqF01MWU2pDaJZiojg7q709z0o8j%2BmosJWxkMfJCr4jILk5YdMhzEzL2Xp4fh7OmsYUxTEAgoGkSALyf%2Ft96bf45GEyKVDBvtO6ai%2Bjp0GFe0TIJlyDZrNesMTCZkHDi5UzoTkyGA4G30yc1c%3D%7CADC_lOm9QSd2ubL6Cb8txCG8JvvOczieO%2BFI5K1A%2BoQIcjlEwG0bpR6Y7vwWbPU3ld1t0NPhOMogWSrNyiZnK0%2BLurNTJOJlnvDymw8eFKqO%2BsrN2vWiWeFtV7SjFZGsig5svUurGwkeJc45w%2FrRLO8G6DwvUdnZiR1LrV1%2F05et4twW77YDmxrRufL63j1fhUXUZH6mM8e4Qq3STDvnDhIH1mQ3FCXjgfc7goz%2FYtyKvP%2F8UvHT4A%2F1AlCqmQuBzBeXWcQaPVH2KpmrWf5cKPLWEnPOU9dMgy%2BMMKPKI1RGrsxI6fLOsVw0tpgsgcMjknaDU3yFIfhhfjZywSLnuo2R%2BW53GSNbrhqrApkjpYN%2BeMDMJbjVshr9RW3zofUDqZpgR6xTwgRlCYrukd5k1VcIrxYgZECv4ekaDee0GAvOOHASqJaA%2Bo8XOPM7T%2BJI%2Bs1Poi5FgNHuY9fxKHKb3Kot9Mm6GlbzZdZtjKaTqLv3DYQOXI4vLkyoaOsNyTjvJpC7Mcshb7N9Rm4J%2FdTeC953Rd%2B6%2Bn7ER%2BRZpdihEWmC8hc8d8MDn%2BFoKKFF3RUPtjy%2BQ%2Fv%2FDGdahZcOmMG0uJeaqwpuS15LKO59G7EwSRm11ge6JEs4uw3geOKxDGY%2Bp4P68tZhG%2BI%2FQJZDhcTApZpI2Q%3D%3D',
                     'shshshfp':'c4b859998ff9d3bd6a72c552169fc199',
                     'shshshfpb':'15129ec12414d45df9556cc9774f71d133e286f13285539825aecfb037',
                     '__wga':'1540703164135.1540703164135.1540703164135.1540703164135.1.1',
                     'shshshfpa':'9ec80a26-3a30-04e4-e86f-d6db8fe6e240-1540703164',
                     'webp':'0',
                     'cartNum':'0',
                     'visitkey':'28669990573261742',
                     'wq_addr':'643744556%7C18_1482_48938_52586%7C%u6E56%u5357_%u957F%u6C99%u5E02_%u5F00%u798F%u533A_%u57CE%u533A%7C%u6E56%u5357%u957F%u6C99%u5E02%u5F00%u798F%u533A%u57CE%u533A%u8F66%u7AD9%u5317%u8DEF609%u53F7%u9644%u8FD1%u56DB%u65B9%u576A%u7EA2%u5546%u5EFA%u6750%u5E02%u573AD1%u680B202%7C113.00705%2C28.2366',
                     }
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

