import allure
import pytest
from base.base_test import BaseTest

@allure.parent_suite("Страница 'Pim'")
class TestPimPanel(BaseTest):

    @allure.title("проверка ввода имени")
    @allure.severity("medium")
    @pytest.mark.smoke
    def test_write_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_pim_link()
        self.pim_page.is_opened()
        self.pim_page.write_employee_id("0295")
        self.pim_page.submit_button()
        self.pim_page.check_id_result()
        self.pim_page.make_screenshot("Success")

    @allure.title("проверка ввода не только имени ")
    @allure.severity("medium")
    @allure.mark.smoke
    def test_write_sup_name_id(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_pim_link()
        self.pim_page.is_opened()
        self.pim_page.write_employee_name("Sobaka")
        self.pim_page.write_supervisor_name("SObakas")
        self.pim_page.write_employee_id("0989")
        self.pim_page.make_screenshot("Succeess")

