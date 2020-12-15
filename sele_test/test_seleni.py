import yaml
from selenium import webdriver


def test_get_cookic():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    cookic = driver.get_cookies()
    with open('data.yaml', 'w', encoding='utf-8') as f:
        ys = yaml.safe_dump(cookic, f)
    print(ys)


def test_web():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    with open('data.yaml', encoding='uts-8') as f:
        datas = yaml.safe_load(f)
    for cookic in datas:
        driver.add_cookie(cookic)
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')

    driver.quit()
