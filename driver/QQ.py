from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').send_keys('454216847')
driver.find_element_by_id('p').send_keys('gy1988711')#password
driver.find_element_by_id('login_button').click()

