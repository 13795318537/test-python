from selenium.webdriver.common.by import By

from sele_test.selenium_po.page.Base_page import BasePage
from sele_test.selenium_po.page.contact_page import ContactPage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact_page(self):
        self.find(By.ID, 'menu_contacts').click()

        return ContactPage(self.driver)

    def main_add_member(self):
        from sele_test.selenium_po.page.add_member_page import AddMemberPage
        # self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        ele = (By.CSS_SELECTOR, "#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(1)")
        self.wait_click(ele, 10)
        while True:
            self.find(By.CSS_SELECTOR, "#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(1)").click()
            elem = self.finds(By.ID, "username")
            if len(elem) > 0:
                break
        return AddMemberPage(self.driver)

