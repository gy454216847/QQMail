import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from Website.test_case.model.function import *
import time
report_dir ='./test_report'
test_dir = './test_case'

print('start run test case....')
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir +'/'+now + ' result.html'
print(report_name)



with open(report_name, 'wb') as file:
    runner = HTMLTestRunner(stream=file,
                              title='测试报告',
                              description='QQ邮箱登录',
                              verbosity=2,
                              tester='GanYu')
    runner.run(discover)
latest_report=latest_report(report_dir)

send_mail(latest_report)
# send_mail(latest_report)
print('test end!')

