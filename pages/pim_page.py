import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from Practice.base.base_page import BasePage
from Practice.config.links import Links
from Practice.config.locators import PimLocators


class PimPage(BasePage, PimLocators):

    PAGE_URL = Links.PIM_PAGE

    # def base_write_in_field(self, name, locator):
    #         field = self.wait.until(EC.element_to_be_clickable(locator))
    #         field.send_keys(Keys.COMMAND + "a")
    #         field.send_keys(Keys.BACKSPACE)
    #         field.send_keys(name)
    #         return name

    def write_employee_name(self, new_name):
        with allure.step(f"'ввод имени работника {new_name}'"):
            field = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_NAME_FIELD))
            field.send_keys(Keys.COMMAND + "a")
            field.send_keys(Keys.BACKSPACE)
            field.send_keys(new_name)
            self.name = new_name


    def write_supervisor_name(self, new_sup_name):
        with allure.step(f"'ввод имени супервайзера {new_sup_name}'"):
            field = self.wait.until(EC.element_to_be_clickable(self.SUPERVISOR_NAME_FIELD))
            field.send_keys(Keys.COMMAND + "a")
            field.send_keys(Keys.BACKSPACE)
            field.send_keys(new_sup_name)
            self.sup_name = new_sup_name


    def write_employee_id(self, new_id):
        with allure.step(f"'ввод id работника {new_id}'"):
            field = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_ID_FIELD))
            field.send_keys(Keys.COMMAND + "a")
            field.send_keys(Keys.BACKSPACE)
            field.send_keys(new_id)
            self.id = new_id


    @allure.step("Выбор статус работника")
    def choose_employee_status(self, x):
        """1 - freelance/ 2 - full-time contract/ 3 - full-time permanent"""
        self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_STATUS)).click()
        if x == 1:
            self.wait.until(EC.element_to_be_clickable(self.STATUS_FREELANCE)).click()
            assert self.wait.until(EC.text_to_be_present_in_element(self.EMPLOYEE_STATUS, "Freelance")), "Выбран другой статус"
        elif x == 2:
            self.wait.until(EC.element_to_be_clickable(self.STATUS_FULL_TIME_CONTRACT)).click()
            assert self.wait.until(EC.text_to_be_present_in_element(self.EMPLOYEE_STATUS, "Full-Time Contract")), "Выбран другой статус"
        else:
            self.wait.until(EC.element_to_be_clickable(self.STATUS_FULL_TIME_PERMANENT)).click()
            assert self.wait.until(EC.text_to_be_present_in_element(self.EMPLOYEE_STATUS, "Full-Time Permanent")), "Выбран другой статус"


    @allure.step("Выбор включение работника")
    def choose_include(self, x):
        """1 - Current and Past Employees Only/ 2 - Past Employees Only"""
        self.wait.until(EC.element_to_be_clickable(self.INCLUDE)).click()
        if x == 1:
            self.wait.until(EC.element_to_be_clickable(self.CURRENT_EMPLOYEE)).click()
            assert self.wait.until(EC.text_to_be_present_in_element(self.INCLUDE, "Current and Past Employees Only")), "Выбран другой инклуд"
        else:
            self.wait.until(EC.element_to_be_clickable(self.PAST_EMPLOYEE)).click()
            assert self.wait.until(EC.text_to_be_present_in_element(self.INCLUDE, "Past Employees Only")), "Выбран другой инклуд"


    @allure.step("Выбор названия работы")
    def choose_job_tittle(self, x):
        """1 - Account Assistant/ 2 - Automaton Tester"""
        self.wait.until(EC.element_to_be_clickable(self.JOB_TITTLE)).click()
        if x == 1:
            self.wait.until(EC.element_to_be_clickable(self.JOB_TITTLE_ACCOUNT_ASSISTANT)).click()
            assert self.wait.until(EC.text_to_be_present_in_element(self.JOB_TITTLE, "Account Assistant")), "Выбрана не та работа"
        else:
            self.wait.until(EC.element_to_be_clickable(self.JOB_TITTLE_AUTOMATION_TESTER)).click()
            assert self.wait.until(EC.text_to_be_present_in_element(self.JOB_TITTLE, "Automaton Tester")), "Выбрана не та работа"


    @allure.step("Выбор саб юнита")
    def choose_sub_unit(self , x):
        """1 - OrangeHRM/ 2 - Administration"""
        self.wait.until(EC.element_to_be_clickable(self.SUB_UNIT)).click()
        if x == 1:
            self.wait.until(EC.element_to_be_clickable(self.ORANGEHRM_UNIT)).click()
            assert self.wait.until(EC.text_to_be_present_in_element(self.SUB_UNIT, "OrangeHRM")), "Выбран не тот юнит"
        else:
            self.wait.until(EC.element_to_be_clickable(self.ADMINISTRATION_UNIT)).click()
            assert self.wait.until(EC.text_to_be_present_in_element(self.SUB_UNIT, "Administration")), "Выбран не тот юнит"

    @allure.step("Нажать кнопку поиска")
    def submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    @allure.step("Проверка введнёного айди")
    def check_id_result(self):
        text = self.wait.until(EC.element_to_be_clickable(self.ID_RESULT)).text
        assert text == self.name, "Имя не совпадает"

    def check_first_name_result(self):
        pass

    def check_last_name_result(self):
        pass

    def check_job_tittle_result(self):
        pass

    def check_employment_status_result(self):
        pass

    def check_sub_unit_result(self):
        pass

    def check_supervisor_result(self):
        pass
