import allure
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from config.links import Links
from config.locators import TimeLocators


class TimePage(BasePage, TimeLocators):

    PAGE_URL = Links.TIME_PAGE

