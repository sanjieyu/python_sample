
# Author:Yi Sun(Tim) 2018

'''
下面以实现我的163邮箱登录为测试用例，两个测试点分别是用户名为空和登录邮箱格式错误，
把测试的数据存储在Excel中，测试用到的数据直接从Excel中读取
'''

import xlrd
import unittest
from selenium import webdriver
import time as t

def readExcel(row):
    book = xlrd.open_workbook('163.xlsx','r')
    table = book.sheet_by_index(0)
    return table.row_values(row)

class MailLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://mail.163.com/")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def login(self,username,password):
        t.sleep(2)
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('login').click()

    def getLoginError(self):
        '''返回点击登录按钮后的错误提示信息'''
        t.sleep(2)
        loginError = self.driver.find_element_by_id('kw')
        return loginError.text

    def test_163_login_null(self):
        '''验证：测试用户名和密码都为空的错误提示信息'''
        t.sleep(2)
        self.login(readExcel(1)[0],readExcel(1)[1])
        self.assertEqual(self.getLoginError(),readExcel(1)[2])

    def test_163_login_format(self):
        '''验证：测试用户名邮箱格式不正确的错误提示信息'''
        self.login(readExcel(2)[0],readExcel(2)[1])
        self.assertEqual(self.getLoginError(),readExcel(2)[2])

if __name__ == '__main__':
    unittest.main(verbosity=2)
