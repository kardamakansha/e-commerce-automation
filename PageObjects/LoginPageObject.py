import time
from selenium import webdriver
from PageObjects.SignUpPageObject import SignUpPageObject
from PageObjects.HomePageObject import HomePageObject


class LoginPageObject:
    user_email_text_xpath = "//input[@data-qa= 'login-email']"
    Password_text_xpath = "//input[@data-qa= 'login-password']"
    Login_button_xpath = "//button[@data-qa= 'login-button']"
    user_not_found_message = "Your email or password is incorrect!"


    def __init__(self, driver):
        self.driver = driver
        self.signPO = SignUpPageObject(self.driver)
        self.homePO = HomePageObject(self.driver)

    def loginWithUsernameAndPassword(self, username, password):
        #self.homePO.navigateToSighUp_LoginPage()
        self.driver.find_element("xpath", self.user_email_text_xpath).send_keys(username)
        self.driver.find_element("xpath", self.Password_text_xpath).send_keys(password)
        self.driver.find_element("xpath", self.Login_button_xpath).click()





