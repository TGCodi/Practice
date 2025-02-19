import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    ADMIN_WINDOW = ("xpath", "//span[text()='Admin']")
    PIM_WINDOW = ("xpath", "//span[text()='PIM']")
    LEAVE_WINDOW = ("xpath", "//span[text()='Leave']")
    TIME_WINDOW = ("xpath", "//span[text()='Time']")
    RECRUITMENT_WINDOW = ("xpath", "//span[text()='Recruitment']")
    MY_INFO_WINDOW = ("xpath", "//span[text()='My Info']")
    PERFORMANCE_WINDOW = ("xpath", "//span[text()='Performance']")
    DASHBOARD_WINDOW = ("xpath", "//span[text()='Dashboard")
    DIRECTORY_WINDOW = ("xpath", "//span[text()='Directory']")
    MAINTEANCE_WINDOW = ("xpath", "//span[text()='Maintenance']")
    CLAIM_WINDOW = ("xpath", "//span[text()='Claim']")
    BUZZ_WINDOW = ("xpath", "//span[text()='Buzz']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)


    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

