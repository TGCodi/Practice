import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.myinfo_page import MyInfoPage
from pages.admin_page import AdminPage
from pages.time_page import TimePage
from pages.pim_page import PimPage


class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    myinfo_page: MyInfoPage
    admin_page: AdminPage
    time_page: TimePage
    pim_page: PimPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.myinfo_page = MyInfoPage(driver)
        request.cls.admin_page = AdminPage(driver)
        request.cls.pim_page = PimPage(driver)
        request.cls.time_page = TimePage(driver)