import allure
from base.base_page import BasePage
from config.links import Links
from config.locators import AdminPageLocators
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage, AdminPageLocators):

    PAGE_URL = Links.ADMIN_PAGE


    def write_name_in_search_field(self, new_name):
        with allure.step(f"Ввод ника в поиск '{new_name}'"):
            search_name_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
            search_name_field.send_keys(new_name)
            self.name = new_name


    def choose_user_role(self, x):
        with allure.step(f"Выбор роли"):
            user_role = self.wait.until(EC.element_to_be_clickable(self.USER_ROLE))
            user_role.click()

            if x == 1:
                self.wait.until(EC.element_to_be_clickable(self.ADMIN_ROLE)).click()
                self.role = "Admin"
            else:
                self.wait.until(EC.element_to_be_clickable(self.ESS_ROlE)).click()
                self.role = "ESS"


    def choose_status(self, x):
        with allure.step(f"Выбор статуса"):
            status = self.wait.until(EC.element_to_be_clickable(self.STATUS))
            status.click()

            if x == 1:
                self.wait.until(EC.element_to_be_clickable(self.STATUS_ENABLED)).click()
                self.status = "Enabled"
            else:
                self.wait.until(EC.element_to_be_clickable(self.STATUS_DISABLED)).click()
                self.status = "Disabled"



    @allure.step("Клик по кнопке поиска")
    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    @allure.step("Проверка валидности выдачи ника")
    def is_username_search_valid(self):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_RESULT))
        self.wait.until(EC.text_to_be_present_in_element(self.USERNAME_RESULT, self.name))

    @allure.step("Проверка валидности выдачи роли")
    def is_user_role_search_valid(self):
        self.wait.until(EC.visibility_of_element_located(self.USER_ROLE_RESULT))
        self.wait.until(EC.text_to_be_present_in_element(self.USER_ROLE_RESULT, self.role))

    # @allure.step("Проверка валидности выдачи имени")
    # def is_employee_name_search_valid(self):
    #     self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_NAME_RESULT))
    #     self.wait.until(EC.text_to_be_present_in_element_value(self.EMPLOYEE_NAME_RESULT, self.name))

    @allure.step("Проверка валидности выдачи статуса")
    def is_status_search_valid(self):
        self.wait.until(EC.visibility_of_element_located(self.STATUS_RESULT))
        self.wait.until(EC.text_to_be_present_in_element(self.STATUS_RESULT, self.status))

