from selenium import webdriver

from sele_test.selenium_po.page.Base_page import BasePage
from sele_test.selenium_po.page.contact_page import ContactPage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact_page(self):
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()

        return ContactPage(self.driver)
