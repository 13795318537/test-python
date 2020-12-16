from selenium import webdriver
import time


def test_login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    cookies = [{''}]
    for cookic in cookies:
        driver.add_cookie(cookic)
        print(cookic)
    # driver.get("https://work.weixin.qq.com/wework_admin/frame")
    # time.sleep(3)
    # driver.quit()
