from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __init__(self, driver_base: webdriver = None):
        if driver_base is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver_base

        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_click(self, locator, timeout):
        element: WebDriver = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        return element
