from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ContactPage:

    def click_add_member(self):
        from sele_test.selenium_po.page.add_member_page import AddMemberPage
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        while True:
            self.driver.find_element(*ele).click()
            elem = self.driver.find_elements_by_id('username')
            if len(elem) > 0:
                break
        return AddMemberPage()

    def get_member(self):
        pass