import pytest

from Config.config import TestData
from pageObjects.LoginPage import LoginPage
from Tests.test_Base import Test_Base


class Test_LoginPage(Test_Base):

    @pytest.mark.parametrize(

        "username, password",
        [
            (TestData.firstUserName, TestData.password),
            (TestData.secondUserName, TestData.password),
            (TestData.thirdUserName, TestData.password),
            (TestData.fourthUserName, TestData.password),
        ]
    )
    def test_login(self, username, password):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_steps(username, password)
        actualTitle = self.loginPage.get_home_page_title()
        assert actualTitle == TestData.homePageTitle
