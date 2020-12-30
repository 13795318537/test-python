from selenium.webdriver.common.by import By

from sele_test.selenium_po.page.Base_page import BasePage
from sele_test.selenium_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _namea = (By.ID, "username")
    _ida = (By.ID, "memberAdd_acctid")
    _phonea = (By.ID, "memberAdd_phone")

    def add_member(self, name, id, phone):

        self.find(*self._namea).send_keys(name)
        self.find(*self._ida).send_keys(id)
        self.find(By.XPATH, '//input[@type="radio" and @value="2"]').click()
        self.find(*self._phonea).send_keys(phone)
        self.find(By.LINK_TEXT, '保存').click()
        return ContactPage(self.driver)

    # def add_member_fail(self):
    #     self.driver.find_element_by_id('username').send_keys('117111235')
    #     self.driver.find_element_by_id('memberAdd_acctid').send_keys('11739231003')
    #     self.driver.find_element_by_xpath('//input[@type="radio" and @value="2"]').click()
    #     self.driver.find_element_by_id('memberAdd_phone').send_keys('19111112222')
    #     self.driver.find_element_by_link_text('保存').click()
    #     return ContactPage(self.driver)
