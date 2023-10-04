
# Author:Yi Sun(Tim) 2019-12-11

'''获取当前py文件目录，并找到screenshot目录，然后截图保存'''

from selenium import webdriver
import os

def inser_img(driver, filename):
    func_path = os.path.dirname(__file__)
    print(func_path)
    base_dir =  os.path.dirname(func_path)
    print(base_dir)

    # 将路径转化为字符串
    base_dir = str(base_dir)

# 对路径的字符串进行替换
    base_dir = base_dir.replace('\\','/')

    base = base_dir.split('/Test')[0]
    print(base)
    filepath = base + '/Test/Snapshot/' + filename
    print(filepath)
    driver.get_screenshot_as_file(filepath)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    inser_img(driver, 'baidu.png')
