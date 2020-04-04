#!/usr/bin/env python
# @Time : 2020/4/4 20:23 
# @Author : lifei
# @desc:
from atm.case.login import LoginTest
from atm.case.sell import SellTest
from atm.case.customer import CustomerTest
if __name__ == '__main__':
    login_test = LoginTest()
    login_test.test_login_gui()
    login_test.test_login_http()

    SellTest().test_sell()
    customer_test = CustomerTest()
    customer_test.test_add_customer()
    customer_test.test_edit_customer()
