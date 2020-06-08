from selenium import webdriver
from selenium.webdriver.common.by import By
from Website.test_case.page_object.BasePage import Page
import time
class LoginPage(Page):


    username_loc=(By.ID,'u')
    password_loc=(By.ID,'p')
    loginButtonSubmit_loc=(By.ID,'login_button')

    def Login_action(self,username,password):
        self.open()
        self.switch_to()
        self.find_element(*self.username_loc).send_keys(username)
        self.find_element(*self.password_loc).send_keys(password)
        self.find_element(*self.loginButtonSubmit_loc).click()


    LoginPass_loc = (By.ID,'imglogo')
    LoginFail_loc=(By.ID,'err_m')

    def LoginPass_logo(self):
        return self.find_element(*self.LoginPass_loc).is_displayed()

    def LoginFail_hint(self):
        return self.find_element(*self.LoginFail_loc).text

