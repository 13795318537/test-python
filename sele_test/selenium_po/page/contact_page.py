import time

from selenium.webdriver.common.by import By
from sele_test.selenium_po.page.Base_page import BasePage


class ContactPage(BasePage):

    def click_add_member(self):
        from sele_test.selenium_po.page.add_member_page import AddMemberPage
        # self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        self.wait_click(ele, 10)
        while True:
            self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            elem = self.finds(By.ID, "username")
            if len(elem) > 0:
                break
        return AddMemberPage(self.driver)

    def get_member(self):
        time.sleep(1)
        eles = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # print(eles)
        name_list = []
        for values in eles:
            name_list.append(values.get_attribute("title"))
        print(name_list)

        return name_list
