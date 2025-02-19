import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    WINDOW = BasePage.MY_INFO_WINDOW


    @allure.step("Click on 'my info' window")
    def click_my_info_window(self):
        self.wait.until(EC.element_to_be_clickable(self.WINDOW)).click()