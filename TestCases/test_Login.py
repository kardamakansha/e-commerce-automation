import time
from Configration.conftest import json_data
from selenium.webdriver.chrome.options import Options
import pytest

from PageObjects.HomePageObject import HomePageObject
from PageObjects.SignUpPageObject import SignUpPageObject
from selenium import webdriver
from PageObjects.LoginPageObject import LoginPageObject



class Test_Login:
    chrome_options = Options()
    extension_path = "Driver/adblock.crx"
    chrome_options.add_extension(extension_path)
    driver = webdriver.Chrome(options=chrome_options)
    baseURl = "https://automationexercise.com"
    driver.maximize_window()
    homePO = HomePageObject(driver)
    signPO = SignUpPageObject(driver)
    loginPO = LoginPageObject(driver)

    def test_001_signUpNewUser(self, json_data):
        self.driver.get(self.baseURl)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.homePO.navigateToSighUp_LoginPage()
        time.sleep(2)
        user_date = json_data['UserData']
        time.sleep(2)
        self.signPO.signup(user_date)
        time.sleep(4)
        self.driver.close()

    def test_002_loginWithCorrectUserNamePassword(self, json_data):
        self.driver.get(self.baseURl)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.homePO.navigateToSighUp_LoginPage()
        time.sleep(2)
        correct_data = json_data['CorrectUserCredentials']
        username = correct_data['username']
        password = correct_data['password']
        self.loginPO.loginWithUsernameAndPassword(username, password)
