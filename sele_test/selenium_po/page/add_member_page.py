from selenium import webdriver

from sele_test.selenium_po.page.Base_page import BasePage
from sele_test.selenium_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self):
        self.driver.find_element_by_id('username').send_keys('7111235')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('739231003')
        self.driver.find_element_by_xpath('//input[@type="radio" and @value="2"]').click()
        self.driver.find_element_by_id('memberAdd_phone').send_keys('13711112222')
        self.driver.find_element_by_link_text('保存').click()
        return ContactPage(self.driver)

    def add_member_fail(self):
        self.driver.find_element_by_id('username').send_keys('117111235')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('11739231003')
        self.driver.find_element_by_xpath('//input[@type="radio" and @value="2"]').click()
        self.driver.find_element_by_id('memberAdd_phone').send_keys('19111112222')
        self.driver.find_element_by_link_text('保存').click()
        return ContactPage(self.driver)