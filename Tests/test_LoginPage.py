from Config.config import TestData
from pageObjects.LoginPage import LoginPage
from Tests.test_Base import Test_Base


class Test_LoginPage(Test_Base):

    def test_login_page_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_logo_exist()
        assert flag

    def test_login_with_first_valid_input(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_steps(TestData.firstUserName, TestData.password)
        actualTitle = self.loginPage.get_home_page_title()
        assert actualTitle == TestData.homePageTitle

    def test_login_with_second_valid_input(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_steps(TestData.secondUserName, TestData.password)
        actualTitle = self.loginPage.get_home_page_title()
        assert actualTitle == TestData.homePageTitle




