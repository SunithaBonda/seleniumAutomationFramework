from selenium import webdriver
from pages.demosite import DemoSite
import unittest
import pytest



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
#in unittest class name should contain 'test' keyword
class DemoTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ds = DemoSite(self.driver)


    def test_RegisterPage(self):
        self.ds.clickDemoSiteLink()
        self.ds.enterFirstName("sudisha")


    # for execution use below syntax
    # py.test -v  -s  demosite_test.py --browser chrome