from time import sleep
import yaml,os
path=os.path.dirname(os.getcwd())+"\\test_data\\page_data.yaml"
class Page():

    def __init__(self,driver):
        self.driver=driver
        self.file=open(path,"r",encoding="utf-8")
        self.data=yaml.load(self.file)
        self.file.close()
        self.url = self.data['url']
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

if __name__ == '__main__':
    print(os.path.dirname(os.path.dirname(os.getcwd())))