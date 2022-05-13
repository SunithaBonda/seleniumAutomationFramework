from base.selenium_driver import SeleniumDriver
#this class is created to initialize and write methods needed to do
# actions required to login into the webpage as needed.
#in this project we are going to login into http://practice.automationtesting.in.
#for this page it needed to click on MYAccount link and it will navigate to login page .
# login page requires email,password, and click on loginbutton action.
class LoginPage(SeleniumDriver):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #here we are calling SeleniumDriver class as Super class.
        # inorder to call the methods in it we have to write init() also.

        #above  line is for present driver initialization.

    # Locators
    _MyAccount_link = "My Account"
    _email_field = "username"
    _password_field = "password"
    _login_button = "login"

#the below is the standard code we can find in google.
    #def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._MyAccount_link)
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)
# we are modifying the code as below

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


