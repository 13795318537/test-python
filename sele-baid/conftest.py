import pytest
from selenium import webdriver


@pytest.fixture()
def get_open():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
