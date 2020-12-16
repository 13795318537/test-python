import yaml
from selenium import webdriver
import time


class Test_qywx():
    def setup_class(self):
        print('开始测试')

    def test_get_cookic(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
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
        # f_list = self.driver.windows_handles
        # self.driver.switch_to.window(f_list[1])
        time.sleep(3)
        self.driver.find_element_by_link_text('添加成员').click()
        self.driver.find_element_by_id('username').send_keys('测试9')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('103')
        # self.driver.find_element_by_css_selector('#js_contacts101 > div > div.member_colRight > div > div:nth-child(4) > div > form > div.member_edit_formWrap > div:nth-child(1) > div.member_edit_item.member_edit_item_Radios > div.member_edit_item_right > label:nth-child(2) > input').click()
        self.driver.find_element_by_id('memberAdd_phone').send_keys('13299990000')
        # self.driver.find_element_by_link_text('保存并继续添加').click()
