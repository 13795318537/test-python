import yaml
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_qywx():
    def setup_class(self):
        print('开始测试')

    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        cookie = self.driver.get_cookies()
        with open('data.yaml', 'w', encoding='utf-8') as f:
            ys = yaml.safe_dump(cookie, f)
        print(ys)

    def test_web(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        # self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        with open('data.yaml', encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        for cookie in datas:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        while True:
            self.driver.find_element(*ele).click()
            elem = self.driver.find_elements_by_id('username')
            if len(elem) > 0:
                break

            # ele = self.driver.find_element_by_css_selector('.ww_operationBar .js_add_member')
            # ele.click()
            # elem = self.driver.find_elements_by_id('username')
            # if elem > 0:
            #     break

        self.driver.find_element_by_id('username').send_keys('1235')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('11931003')
        self.driver.find_element_by_xpath('//input[@type="radio" and @value="2"]').click()
        self.driver.find_element_by_id('memberAdd_phone').send_keys('10911112222')
        self.driver.find_element_by_link_text('保存并继续添加').click()
        time.sleep(2)
        eles = self.driver.find_element_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')

        name_list = []
        for values in eles:
            name_list.append(values.get_attribute("title"))
        assert "1235" in name_list

        self.driver.quit()
