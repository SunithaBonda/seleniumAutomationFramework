from selenium.webdriver.common.by import By

from base.Final_selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging



class DemoSite(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #URL=http://practice.automationtesting.in
    # Locators
    _DemoSite_link = "Demo Site"
    _FirstName_XPATH = "//*[@id='basicBootstrapForm']/div[1]/div[1]/input"
    """_LastName_XPATH = "//*[@id='basicBootstrapForm']/div[1]/div[2]/input"
    _Address_XPATH= "//*[@id='basicBootstrapForm']/div[2]/div/textarea"
    _EmailAddress_XPATH="//*[@id='eid']/input"
    _Phone_XPATH="//*[@id='basicBootstrapForm']/div[4]/div/input"
    _MaleGenderRD_XPATH="//*[@value='Male']"
    _FemaleGenderRD_XPATH = "//*[@value='FeMale']"
    _HobbiesCricketchkbx_id="checkbox1"
    _HobbiesMovieschkbx_id="checkbox2"
    _HobbiesHockeychkbx_id="checkbox3"   """
#here we are using methods written in Final_selenium_driver.py
    def clickDemoSiteLink(self):
        self.elementClick(self._DemoSite_link, locatorType="link")
    def enterFirstName(self, FirstName):
        self.send_keys(FirstName, self._FirstName_XPATH)


    def register(self, FirstName):
        self.clickDemoSiteLink()
        self.enterFirstName(FirstName)


