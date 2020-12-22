from selenium import webdriver

from sele_test.selenium_po.page.contact_page import ContactPage


class AddMemberPage:

    def add_member(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        self.driver.find_element_by_id('username').send_keys('1235')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('11931003')
        self.driver.find_element_by_xpath('//input[@type="radio" and @value="2"]').click()
        self.driver.find_element_by_id('memberAdd_phone').send_keys('10911112222')
        self.driver.find_element_by_link_text('保存并继续添加').click()
        return ContactPage()