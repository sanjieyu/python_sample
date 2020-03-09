
# Author:Yi Sun(Tim) 2020-03-09

'''Data Driven Test Sample'''

import unittest
from selenium import webdriver
from ddt import data,unpack,ddt

def getData():
    '''数据分离出来放到列表中'''
    return [
        ['', '' u'请输入邮箱名'],
        ['', 'admin', u'请输入邮箱名']
        ['admin', '', u'您输入的邮箱名格式不正确']]

@ddt
class SinaLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://mail.sina.com.cn/")
        self.driver.implicitly_wait()

    def tearDown(self):
        self.driver.quit()

    @data(*getData())
    @unpack

    def test_login(self,username,password,result):
        '''验证：测试邮箱登录的Ｎ种情况'''
        self.driver.find_element_by_id('freename').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id(u'登录').click()
        divText = self.driver.find_element_by_id('text').text
        self.assertEqual(divText,result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
