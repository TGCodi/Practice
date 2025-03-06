import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_page import BasePage
from config.links import Links
from config.locators import TimeLocators


class TimePage(BasePage, TimeLocators):

    PAGE_URL = Links.TIME_PAGE

    def write_employee_name(self, new_name):
        with allure.step(f"Ввод имени '{new_name}'"):
            field = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_NAME_FIELD))
            field.send_keys(Keys.COMMAND + "a")
            field.send_keys(Keys.BACKSPACE)
            field.send_keys(new_name)
            self.name = new_name

    def check_auto_complete(self):
        with allure.step(f"проверка авподстановки '{self.name}'"):
            self.wait.until(EC.element_to_be_clickable(self.AUTOCOMPLETE_RESULT))
            assert self.wait.until(EC.text_to_be_present_in_element(self.EMPLOYEE_NAME_FIELD, self.name)), "нет имен для автоподстановки"



