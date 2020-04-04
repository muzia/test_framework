#!/usr/bin/env python
# @Time : 2020/4/4 18:57 
# @Author : lifei
# @desc:
from selenium import webdriver
import time, requests, os


class Utility:
    driver = None
    session = None

    def __init__(self):
        pass

    @classmethod
    def get_webdriver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Firefox()
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
            cls.driver.get("http://127.0.0.1:8080/WoniuSales-20180508-V1.4-bin/")
            time.sleep(5)
        return cls.driver

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.session = requests.session()
        return cls.session

    @classmethod
    def write_result(cls, case, result):
        path = os.path.abspath('..') + '/result/mytest.txt'
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        line = now + ',' + case + ',' + result + '\n'
        with open(path, 'a+', encoding='utf-8') as f:
            f.write(line)

    @classmethod
    def assert_result(cls, case, expect, actual):
        if expect == actual:
            cls.write_result(case, '成功')
        else:
            cls.write_result(case, '失败')

    # 把一个post请求上下文的key=value&key=value的普通字符串转换为一个字典对象,供request发请求用
    @classmethod
    def build_dict(self, string):
        dict = {}
        list = string.split('&')
        for item in list:
            key = item.split('=')[0]
            value = item.split('=')[1]
            dict[key] = value
        return dict
