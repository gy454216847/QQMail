import unittest
from HTMLTestRunnerNew import HTMLTestRunner
import time
import smtplib                         # 发送邮件模块
from email.mime.text import MIMEText   # 定义邮件内容
from email.header import Header        # 定义邮件标题
import os


def inser_img(driver, filename):
    # 获取当前模块所在路径
    func_path = os.path.dirname(__file__)
    # print("func_path is %s" %func_path)

    # 获取test_case目录
    base_dir = os.path.dirname(func_path)
    # print("base_dir is %s" %base_dir)

    # 将路径转化为字符串
    base_dir = str(base_dir)

    # 对路径的字符串进行替换
    base_dir = base_dir.replace('\\', '/')
    # print(base_dir)

    # 获取项目文件的根目录路径
    base = base_dir.split('/Website')[0]
    # print(base)

    # 指定截图存放路径
    filepath = base + '/Website/test_report/screenshot/' + filename
    # print(filepath)
    driver.get_screenshot_as_file(filepath)


def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + "\\" + fn))
    print("The latest report is:" + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content = f.read()
    f.close()

    smtpserver = 'smtp.exmail.qq.com'

    user = 'ganyu@lookdoor.com'
    password = 'Gy1988711'

    sender = 'ganyu@lookdoor.com'
    receives = 'ganyu@lookdoor.com'

    subject = '自动化测试报告'

    msg = MIMEText(mail_content,'html','utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = sender
    msg['To'] = receives

    smtp = smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user,password)

    print("Start send email....")
    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()
    print("Send email end")



    # h获取最新测试报告
    latest_report = latest_report(report_dir)
    # 发送邮件报告
    send_mail(latest_report)




