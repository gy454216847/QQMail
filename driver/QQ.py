import os

from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(chrome_options=option)
driver.get('https://mail.qq.com/')
driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').send_keys('454216847')
driver.find_element_by_id('p').send_keys('gy1988711')  # password
driver.find_element_by_id('login_button').click()
