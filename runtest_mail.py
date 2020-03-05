# Author:Yi Sun(Tim) 2019-11-05

'''整合自动化测试发送测试报告'''

import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#======查找测试目录，找到最新生成的测试报告======
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new

# ======定义发送邮件========
def send_mail(file_new):
　　#方法１打开文件
    with open(file_new, 'rb') as f:
        mail_body = f.read()
        print(mail_body)

    ''' 方法２打开文件，推荐方法１
    f = open(file_new, 'rb')
        mail_body = f.read()
        print(mail_body)
    f.close()
     '''
    smtpserver = 'smtp.163.com'
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    user = 'jerrymayi78@163.com'
    password = 'xxxx'
    sender = 'jerrymayi78@163.com'
    receiver = 'sunyib@cnsuning.com'
    subject = 'auto send the test report'

    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg['From'] = 'jerrymayi78@163.com'
    msg['To'] = 'sunyib@cnsuning.com'
    msg['Subject'] = Header(subject, 'utf-8')
    smtp.login(user, password)
    print('Start to send')
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('Mail send out')

if __name__ == "__main__":
    test_dir = "C:\\Users\\18030056\\PycharmProjects\\automation\\testbag"
    test_report = "C:\\Users\\18030056\\PycharmProjects\\automation\\testbag"

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='interface_test1.py')

    now = time.strftime("%Y-%m-%d_%H_%M_%S")

    #定义报告存放路径
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')

    #定义测试报告
    runner = HTMLTestRunner(stream=fp, title='xxx_report', description='test_excute')

    #运行测试
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)
