
from selenium import webdriver
from pages.l_login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
#in unittest class name should contain 'test' keyword
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
    @pytest.mark.sanity
    #@pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login("varniktech@gmail.com", "varnik20@123")
        result = self.lp.verifyLoginSuccessful()
        assert result == False
    @pytest.Mark.regression
    #@pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("varniktech@email.com", "varnik20@123")
        result = self.lp.verifyLoginFailed()
        assert result == False


    # for execution use below syntax
    # py.test -v -s l_login_tests.py --browser chrome