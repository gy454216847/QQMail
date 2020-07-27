from selenium import webdriver


def browser():
    # option = webdriver.ChromeOptions()
    # option.add_argument("headless")
    # driver = webdriver.Chrome(chrome_options=option)
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver


if __name__ == '__main__':
    browser()
