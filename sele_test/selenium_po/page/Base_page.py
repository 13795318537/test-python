from selenium import webdriver


class BasePage:
    def __init__(self, base_url: webdriver = None):
        if base_url is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        else:
            self.driver = base_url
