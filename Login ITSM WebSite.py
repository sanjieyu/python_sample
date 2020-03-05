
# Author:Yi Sun(Tim) 2019-07-12

'''Login ITSM WebSite'''

from selenium import webdriver


class Login():
    def __init__(self):
        self.fp = None
        self.username = None
        self.password = None

    def openfile(self):
        try:
            fileName = input('pls input a file; ')
            self.fp = open("%s.txt" % fileName, 'r')
        except FileNotFoundError as rr:
            print("%s file not found" % fileName, str(rr))

    def readfile(self):
        if self.fp:
            lines = self.fp.readlines()
            for i in lines:
                self.username = lines[0]
                self.password = lines[1]
            print(self.username, self.password)
            return self.username, self.password


class setUp(Login):
    def setup(self):
        print("start login")

    def login(self, driver,loader):
        self.driver = driver
        self.loader = loader
        self.driver.find_element_by_id('username').send_keys(self.loader.username)
        self.driver.find_element_by_id('password').send_keys(self.loader.password)
        self.driver.find_element_by_class_name('login-button').click()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://itsm.cnsuning.com")
    login1 = Login()
    login1.openfile()
    login1.readfile()
    login2 = setUp()
    login2.login(driver,login1)
