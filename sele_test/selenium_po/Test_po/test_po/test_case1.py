import pytest

from sele_test.selenium_po.page.main_page import MainPage


class TestLogin:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name, id, phone", [('ddd11', 'id1111', '13110001111')])
    def test_login(self, name, id, phone):
        # name = '5544'
        # id = 'wreterte'
        # phone = '13299991111'
        namelist = self.main.goto_contact_page().click_add_member().add_member(name, id, phone).get_member()
        assert name in namelist
