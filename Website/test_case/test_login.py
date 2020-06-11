
import unittest
from Website.test_case.model import function,myunit
from Website.test_case.page_object.LoginPage import LoginPage
import time

class LoginTest(myunit.StartEnd):

    def test_login1_normal(self):
        print('test_login_normal is start....')
        po=LoginPage(self.driver)
        username ='454216847'
        password = 'GanYu1988711'
        po.Login_action(username,password)


        #断言

        self.assertTrue(po.LoginPass_logo())
        function.insert_img(self.driver, 'QQMail_login_normal.png')
        self.driver.quit()

        print("test_login1_normal is test end!")

    def test_login2_fail(self):
        print('test_login_normal is start....')
        po = LoginPage(self.driver)
        username = '454216847'
        password = '123456'
        po.Login_action(username, password)
        self.assertEqual(po.LoginFail_hint(), '你输入的帐号或密码不正确，请重新输入。')
        function.insert_img(self.driver, 'QQMail_login_fail.png')

        self.driver.quit()
        print("test_login1_fail is test end!")

if __name__ == '__main__':
    unittest.main()