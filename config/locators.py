

class AdminPageLocators:

    USERNAME_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    USERNAME_RESULT = ("xpath", "(//div[@class='oxd-table-cell oxd-padding-cell'])[2]/div")

    USER_ROLE = ("xpath", "(//div[text()='-- Select --'])[1]" )
    ADMIN_ROLE = ("xpath", "(//div[@class='oxd-select-option']/span)[1]")
    ESS_ROlE = ("xpath", "(//div[@class='oxd-select-option']/span)[2]")
    USER_ROLE_RESULT = ("xpath", "(//div[@class='oxd-table-cell oxd-padding-cell'])[3]/div" )

    EMPLOYEE_NAME_FIElD = ("xpath", "//input[@placeholder='Type for hints...']")
    EMPLOYEE_NAME_RESULT = ("xpath", "(//div[@class='oxd-table-cell oxd-padding-cell'])[4]/div")

    STATUS = ("xpath", "(//div[text()='-- Select --'])[2]")
    STATUS_ENABLED = ("xpath", "//span[text()='Enabled']")
    STATUS_DISABLED = ("xpath", "//span[text()='Disabled']")
    STATUS_RESULT = ("xpath", "(//div[@class='oxd-table-cell oxd-padding-cell'])[5]/div")

    RESET_BUTTON = ("xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']")
    SEARCH_BUTTON = ("xpath", "//button[@type='submit']")

    HIDE_SYSTEM_USERS = ("xpath", "(//button[@class='oxd-icon-button'])[2]")

class DashboardPageLocators:

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")
    ADMIN_BUTTON = ("xpath", "//span[text()='Admin']")


class MyInfoPageLocators:

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    MIDDLE_NAME_FIELD = ("xpath", "//input[@name='middleName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    NICKNAME_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

class LoginPageLocators:

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
