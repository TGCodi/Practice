import allure
from base.base_page import BasePage
from config.links import Links
from config.locators import DashboardPageLocators
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage, DashboardPageLocators):

    PAGE_URL = Links.DASHBOARD_PAGE


    @allure.step("перейти на страницу 'My Info'")
    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()


    @allure.step("перейти на страницу 'Admin'")
    def click_admin_link(self):
        self.wait.until(EC.element_to_be_clickable(self.ADMIN_BUTTON)).click()


    @allure.step("перейти на страницу 'Pim'")
    def click_pim_link(self):
        self.wait.until(EC.element_to_be_clickable(self.PIM_BUTTON)).click()


    @allure.step("перейти на страницу 'Time'")
    def click_time_link(self):
        self.wait.until(EC.element_to_be_clickable(self.TIME_BUTTON)).click()