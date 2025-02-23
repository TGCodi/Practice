import random
import allure
import pytest
from base.base_test import BaseTest

@allure.parent_suite("Страница 'Админ'")
class TestAdminPanel(BaseTest):

    @allure.title("Поиск по никнейму")
    @allure.severity("medium")
    @pytest.mark.smoke
    def test_search_by_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_admin_link()
        self.admin_page.is_opened()
        self.admin_page.write_name_in_search_field("Admin}")
        self.admin_page.click_search_button()
        self.admin_page.is_username_search_valid()
        self.admin_page.make_screenshot("Success")

    @allure.title("Смена по роле")
    @allure.severity("medium")
    @pytest.mark.smoke
    def test_search_by_role(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_admin_link()
        self.admin_page.is_opened()
        self.admin_page.choose_user_role(1)
        self.admin_page.click_search_button()
        self.admin_page.is_user_role_search_valid()
        self.admin_page.make_screenshot("Success")

    @allure.title("Поиск по статусу")
    @allure.severity("medium")
    @pytest.mark.smoke
    def test_search_by_status(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_admin_link()
        self.admin_page.is_opened()
        self.admin_page.choose_status(2)
        self.admin_page.click_search_button()
        self.admin_page.is_status_search_valid()
        self.admin_page.make_screenshot("Success")
