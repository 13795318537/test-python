from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class Test_alert:

    def test_open(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(3)


