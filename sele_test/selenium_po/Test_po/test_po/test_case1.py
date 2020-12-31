import pytest

from sele_test.selenium_po.page.main_page import MainPage


class TestLogin:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name, id, phone", [('qwe', 'qwe', '13322221111')])
    def test_login(self, name, id, phone):
        # name = '5544'
        # id = 'wreterte'
        # phone = '13299991111'
        namelist = self.main.goto_contact_page().click_add_member().add_member(name, id, phone).get_member()
        assert name in namelist

    @pytest.mark.parametrize("name, id, phone", [("w2", "w2", "13099998888")])
    def test_login2(self, name, id, phone):
        namelist = self.main.main_add_member().add_member(name, id, phone).get_member()
        assert name in namelist
