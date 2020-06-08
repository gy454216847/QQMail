from time import sleep
class Page():

    def __init__(self,driver):
        self.driver=driver
        self.url = 'https://mail.qq.com/'
        self.timeout = 20

    def _open(self,url):
        print('The page is:%s'%url)
        # self.driver.maximize_window()
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        assert self.driver.current_url == url,'Did not land on %s' %url

    def open(self):
        self._open(self.url)

    def switch_to(self):
        self.driver.switch_to.frame('login_frame')

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

