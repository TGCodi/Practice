import allure
from Practice.base.base_page import BasePage
from Practice.config.links import Links
from Practice.config.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage, LoginPageLocators):

    PAGE_URL = Links.LOGIN_PAGE

    @allure.step("Ввод логина")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Подтвердить вход")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()