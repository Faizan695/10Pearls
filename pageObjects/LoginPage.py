from selenium.webdriver.common.by import By

from Config.config import TestData
from pageObjects.BasePage import BasePage


class LoginPage(BasePage):
    """Locators"""
    usernameInputField = (By.ID, "user-name")
    passwordInputField = (By.ID, "password")
    loginBtn = (By.ID, "login-button")
    loginPageLogo = (By.CLASS_NAME, "login_logo")
    homePageTitle = (By.CLASS_NAME, "title")

    """Constructor of the page class"""

    def __int__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.baseUrl)

        """Page Actions"""

    """Used to get login page logo"""

    def is_logo_exist(self):
        return self.is_visible(self.loginPageLogo)

    """Used to perform login action"""

    def login_steps(self, username, password):
        self.send_keys(self.usernameInputField, username)
        self.send_keys(self.passwordInputField, password)
        self.click_action(self.loginBtn)

    """Used to get home page title"""

    def get_home_page_title(self):
        text = self.get_element_text(self.homePageTitle)
        return text
