import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):
    #@pytest.mark.sanity
    def test_validLogin(self):
        baseURL = "http://practice.automationtesting.in"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp=LoginPage(driver)
        lp.login("varniktech@gmail.com", "varnik20@123")
