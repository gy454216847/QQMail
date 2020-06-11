from selenium import webdriver

def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

if __name__ == '__main__':
    browser()
