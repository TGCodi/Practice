import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from config.links import Links
from config.locators import MyInfoPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MyInfoPage(BasePage, MyInfoPageLocators):

    PAGE_URL = Links.MYINFO_PAGE

    def change_first_name(self, new_name):
        with allure.step(f"Смена имени на '{new_name}'"):
            field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            field.send_keys(Keys.COMMAND + "a")
            field.send_keys(Keys.BACKSPACE)
            field.send_keys(new_name)
            self.name = new_name


    def change_middle_name(self, new_middle_name):
        with allure.step(f"Смена фамилии на '{new_middle_name}'"):
            field = self.wait.until(EC.element_to_be_clickable(self.MIDDLE_NAME_FIELD))
            field.send_keys(Keys.COMMAND + "a")
            field.send_keys(Keys.BACKSPACE)
            field.send_keys(new_middle_name)
            self.middle_name = new_middle_name


    def change_last_name(self, new_last_name):
        with allure.step(f"Смена отчества на '{new_last_name}'"):
            field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD))
            field.send_keys(Keys.COMMAND + "a")
            field.send_keys(Keys.BACKSPACE)
            field.send_keys(new_last_name)
            self.last_name = new_last_name


    def change_nickname(self, new_nickname):
        with allure.step(f"Смена никнейма на '{new_nickname}'"):
            field = self.wait.until(EC.element_to_be_clickable(self.NICKNAME_FIELD))
            field.send_keys(Keys.COMMAND + "a")
            field.send_keys(Keys.BACKSPACE)
            field.send_keys(new_nickname)
            self.nickname = new_nickname

    @allure.step("Сохранить изменения")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Проверка сохранения имени")
    def is_first_name_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))

    @allure.step("Проверка сохранения фамилии")
    def is_middle_name_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.MIDDLE_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.MIDDLE_NAME_FIELD, self.middle_name))

    @allure.step("Проверка сохранения отчества")
    def is_last_name_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.LAST_NAME_FIELD, self.last_name))

    @allure.step("Проверка сохранения ника")
    def is_nickname_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.NICKNAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.NICKNAME_FIELD, self.nickname))