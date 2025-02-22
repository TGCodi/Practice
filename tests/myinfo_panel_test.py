import random
import allure
import pytest
from base.base_test import BaseTest

@allure.parent_suite("Страница 'Моё инфо'")
class TestMyInfoPanel(BaseTest):

    @allure.title("Смена имени")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_change_first_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.myinfo_page.is_opened()
        self.myinfo_page.change_first_name(f"Test {random.randint(1, 100)}")
        self.myinfo_page.save_changes()
        self.myinfo_page.is_first_name_saved()
        self.myinfo_page.make_screenshot("Success")

    @allure.title("Смена фамилии")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_change_middle_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.myinfo_page.is_opened()
        self.myinfo_page.change_middle_name(f"Test {random.randint(1, 100)}")
        self.myinfo_page.save_changes()
        self.myinfo_page.is_middle_name_saved()
        self.myinfo_page.make_screenshot("Success")

    @allure.title("Смена отчества")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_change_last_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.myinfo_page.is_opened()
        self.myinfo_page.change_last_name(f"Test {random.randint(1, 100)}")
        self.myinfo_page.save_changes()
        self.myinfo_page.is_last_name_saved()
        self.myinfo_page.make_screenshot("Success")

    @allure.title("Смена никнейма")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_change_nickname(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.myinfo_page.is_opened()
        self.myinfo_page.change_nickname(f"Test {random.randint(1, 100)}")
        self.myinfo_page.save_changes()
        self.myinfo_page.is_nickname_saved()
        self.myinfo_page.make_screenshot("Success")


    @allure.title("Смена обязательных полей")
    @allure.severity("High")
    @pytest.mark.smoke
    def test_change_nickname(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.myinfo_page.is_opened()
        self.myinfo_page.change_first_name(f"Test {random.randint(1, 100)}")
        self.myinfo_page.change_middle_name(f"Test {random.randint(1, 100)}")
        self.myinfo_page.save_changes()
        self.myinfo_page.is_first_name_saved()
        self.myinfo_page.is_middle_name_saved()
        self.myinfo_page.make_screenshot("Success")


