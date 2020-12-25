from selenium import webdriver
from selenium.webdriver.common.by import By

from sele_test.selenium_po.page.Base_page import BasePage
from sele_test.selenium_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self, name, id, phone):
        namea = (By.ID, "username")
        ida = (By.ID, "memberAdd_acctid")
        phonea = (By.ID, "memberAdd_phone")

        self.driver.find_element(*namea).send_keys(name)
        self.driver.find_element(*ida).send_keys(id)
        self.driver.find_element_by_xpath('//input[@type="radio" and @value="2"]').click()
        self.driver.find_element(*phonea).send_keys(phone)
        self.driver.find_element_by_link_text('保存').click()
        return ContactPage(self.driver)

    # def add_member_fail(self):
    #     self.driver.find_element_by_id('username').send_keys('117111235')
    #     self.driver.find_element_by_id('memberAdd_acctid').send_keys('11739231003')
    #     self.driver.find_element_by_xpath('//input[@type="radio" and @value="2"]').click()
    #     self.driver.find_element_by_id('memberAdd_phone').send_keys('19111112222')
    #     self.driver.find_element_by_link_text('保存').click()
    #     return ContactPage(self.driver)
