from selenium import webdriver

def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

if __name__ == '__main__':
    browser()
