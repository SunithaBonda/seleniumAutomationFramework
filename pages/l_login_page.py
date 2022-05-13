#this is page object class which is having all the methods for the web elements present on the webpage.
#we r going to use this class in l_login_test.py to run the test
from base.Final_selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

#this class is created to initialize and write methods needed to do
# actions required to log in into the webpage as needed.
#in this project we are going to log in into http://practice.automationtesting.in.
#for this page it needed to click on MYAccount link and it will navigate to login page .
# login page requires email,password, and click on login button action.
#after logging in we have to write code to check whether it is logged in or not
#this is standard code reusable  for any login page

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # here we are calling SeleniumDriver class as Super class.
        # inorder to call the methods in it we have to write init() also.
        # above  line is for present driver initialization. self.driver=driver

    # Locators
    _MyAccount_link = "My Account"
    _email_field = "username"
    _password_field = "password"
    _login_button = "login"
#here we are using methods written in Final_selenium_driver.py
    def clickMyAccountLink(self):
        self.elementClick(self._MyAccount_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email, password):
        self.clickMyAccountLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/p[1]/strong",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result
