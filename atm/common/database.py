#!/usr/bin/env python
# @Time : 2020/4/4 18:17 
# @Author : lifei
# @desc: 数据库的操作
import pymysql
from pymysql.cursors import SSDictCursor
class DataBase:
    def __init__(self):
        self.conn = pymysql.connect('localhost','root','123456','woniusales',charset='utf8')
        self.cursor = self.conn.cursor(cursor=SSDictCursor)

    def querry_all(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def querry_one(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result


