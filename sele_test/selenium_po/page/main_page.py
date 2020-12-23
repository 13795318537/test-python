from selenium import webdriver

from sele_test.selenium_po.page.contact_page import ContactPage


class MainPage():
    def goto_contact_page(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()

        return ContactPage()
