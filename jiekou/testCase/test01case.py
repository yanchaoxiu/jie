# -*- coding: utf-8 -*-
import json
import unittest

import paramunittest
# import urllib.parse
import urlparse
from jiekou import geturlParams, readExcel
from jiekou.common.configHttp import RunMain

url = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name+u"测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print(u"测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        url1 = "http://www.xxx.com/login?"
        new_url = url1 + self.query
        data1 = dict(urlparse.parse_qsl(urlparse.urlsplit(new_url).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        info = RunMain().run_main(self.method, url, data1)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)# 将响应转换为字典格式
        if self.case_name == 'login':# 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'login_error':# 同上
            self.assertEqual(ss['code'], -1)
        if self.case_name == 'login_null':# 同上
            self.assertEqual(ss['code'], 10001)


