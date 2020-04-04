#!/usr/bin/env python
# @Time : 2020/4/3 10:19 
# @Author : lifei
#@desc:
import time
from selenium import webdriver
from pom_atm.common import Common
class SellPOM:
    # def __init__(self,driver):
    #     self.driver = driver
    def __init__(self):
        self.driver = Common.get_webdriver()
        print('销售模块的Common地址：%d' % id(Common))

    def get_barcode(self):

        return self.driver.find_element_by_id('barcode')

    def get_barcode_button(self):
        return self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/form/button')

    def get_discount_ratio(self):
        return self.driver.find_element_by_css_selector('.discountratio > input')

    def get_buy_count_plus(self):
        return self.driver.find_element_by_css_selector('.buycountInput > button:nth-child(3)')

    def get_customer_phone(self):
        return self.driver.find_element_by_id('customerphone')

    def get_credit_ratio(self):
        return self.driver.find_element_by_id('creditratio')

    def get_submit_button(self):
        return self.driver.find_element_by_id('submit')

    def do_buy_goods(self,barcode,discount_ratio):
        self.get_barcode().send_keys(barcode)
        self.get_barcode_button().click()
        element = self.get_discount_ratio()
        js = 'document.querySelector(".discountratio > input").value="";'
        self.driver.execute_script(js)
        element.send_keys(discount_ratio)
        self.get_buy_count_plus().click()
