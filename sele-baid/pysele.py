from selenium import webdriver
import os

class Test_one:
    def setup(self):
        browser = os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
    def test_a(self):
        url = 'https://www.baidu.com/'
        self.driver.get(url)
        el = self.driver.find_element_by_id('kw')
        el.send_keys('3423423')