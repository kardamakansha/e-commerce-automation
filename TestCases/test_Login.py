import time
from Configration.conftest import json_data
import pytest

from PageObjects.HomePageObject import HomePageObject
from PageObjects.SignUpPageObject import SignUpPageObject
from selenium import webdriver
from PageObjects.LoginPageObject import LoginPageObject



class Test_Login:
    driver = webdriver.Chrome()
    baseURl = "https://automationexercise.com"
    driver.maximize_window()
    homePO = HomePageObject(driver)
    signPO = SignUpPageObject(driver)
    loginPO = LoginPageObject(driver)

    def test_001_signUpNewUser(self, json_data):
        self.driver.get(self.baseURl)
        self.homePO.navigateToSighUp_LoginPage()
        time.sleep(2)
        user_date = json_data['UserData']
        time.sleep(2)
        self.signPO.signup(user_date)
        time.sleep(4)
        self.driver.close()

    def test_002_loginWithCorrectUserNamePassword(self, json_data):
        self.driver.get(self.baseURl)
        self.homePO.navigateToSighUp_LoginPage()
        time.sleep(2)
        correct_data = json_data['CorrectUserCredentials']
        username = correct_data['username']
        password = correct_data['password']
        self.loginPO.loginWithUsernameAndPassword(username, password)
