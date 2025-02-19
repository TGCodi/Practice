import allure
import pytest
from base.base_test import BaseTest

@allure.suite("My info functionality")
class TestProfileChangeName(BaseTest):


    @allure.title("Change name")
    @allure.severity("High")
    @pytest.mark.regression
    def test_change_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_window()
        self.my_info_page.is_opened()
        self.my_info_page.change_name("kek")
        self.my_info_page.save_changes()
        self.my_info_page.is_change_saved()
        self.my_info_page.make_screenshot("Success")

