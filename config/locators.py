

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
    PIM_BUTTON = ("xpath", "//span[text()='PIM']")
    TIME_BUTTON = ("xpath", "//span[text()='Time']")


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

class PimLocators:

    EMPLOYEE_NAME_FIELD = ("xpath", "(//input[@placeholder='Type for hints...'])[1]")
    SUPERVISOR_NAME_FIELD = ("xpath", "(//input[@placeholder='Type for hints...'])[2]")
    EMPLOYEE_ID_FIELD = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")

    JOB_TITTLE = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[3]")
    JOB_TITTLE_ACCOUNT_ASSISTANT = ("xpath", "//span[text()='Account Assistant']")
    JOB_TITTLE_AUTOMATION_TESTER = ("xpath", "//span[text()='Automaton Tester']")

    EMPLOYEE_STATUS = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
    STATUS_FREELANCE = ("xpath", "//span[text()='Freelance']")
    STATUS_FULL_TIME_CONTRACT = ("xpath", "//span[text()='Full-Time Contract']")
    STATUS_FULL_TIME_PERMANENT = ("xpath", "//span[text()='Full-Time Permanent']")

    INCLUDE = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
    CURRENT_EMPLOYEE = ("xpath", "//span[text()='Current and Past Employees']")
    PAST_EMPLOYEE = ("xpath", "//span[text()='Past Employees Only']")

    SUB_UNIT = ("xpath", "(//div[@class='oxd-select-text oxd-select-text--active'])[4]")
    ORANGEHRM_UNIT = ("xpath", "//span[text()='OrangeHRM']")
    ADMINISTRATION_UNIT = ("xpath", "//span[text()='Administration']")

    RESET_BUTTON = ("xpath", "//button[@type='reset']")
    SEARCH_BUTTON = ("xpath", "//button[@type='submit']")

class TimeLocators:
    pass
