from sele_test.selenium_po.page.main_page import MainPage


class TestLogin:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    def test_login(self):
        self.main.goto_contact_page().click_add_member().add_member().get_member()