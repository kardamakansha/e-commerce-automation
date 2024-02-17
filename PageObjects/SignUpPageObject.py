import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.HomePageObject import HomePageObject


class SignUpPageObject:
    user_signup_name_text_xpath = "//input[@data-qa= 'signup-name']"
    user_email_text_xpath = "//input[@data-qa= 'signup-email']"
    user_signup_button_xpath = "//button[@data-qa= 'signup-button']"
    select_title_mrs_xpath = "//input[@id= 'id_gender2']"
    select_title_mr_xpath = "//input[@id= 'id_gender1']"
    user_password_xpath = "//input[@id= 'password']"
    select_day_dropdown_xpath = "//select[@name= 'days']"
    select_month_dropdown_xpath = "//select[@name= 'months']"
    select_year_dropdown_xpath = "//select[@name= 'years']"
    first_name_xpath =  "//input[@id= 'first_name']"
    last_name_xpath = "//input[@id= 'last_name']"
    company_name_xpath = "//input[@id= 'company']"
    address_1_xpath = "//input[@id= 'address1']"
    address_2_xpath = "//input[@id= 'address2']"
    select_country_dropdown_xpath = "//select[@id= 'country']"
    state_xpath  = "//input[@id= 'state']"
    city_xpath = "//input[@id= 'city']"
    zip_code_xpath = "//input[@id= 'zipcode']"
    mobile_number_xpath = "//input[@id= 'mobile_number']"
    create_button_xpath = "//button[text()= 'Create Account']"
    continue_button_xpath = "//a[text()= 'Continue']"
    user_already_exist = "//p[text()='Email Address already exist!']"

    def __init__(self, driver):
        self.driver = driver
        self.homePO = HomePageObject(self.driver)

    def signup(self, userdata):

        self.driver.find_element("xpath", self.user_signup_name_text_xpath).send_keys(userdata['Name'])
        self.driver.find_element("xpath", self.user_email_text_xpath).send_keys(userdata['Email'])
        self.driver.find_element("xpath", self.user_signup_button_xpath).click()
        # check if user already exists
        time.sleep(2)
        try:
            ele = self.driver.find_element("xpath", self.user_already_exist)
            WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(
                (By.XPATH, self.user_already_exist), "Email Address already exist!"))
            print("Sign Up Failed as the User already Exist!")
            assert False
            return
        except NoSuchElementException:
            if userdata['Title'] == 'Mrs':
                self.driver.find_element("xpath", self.select_title_mrs_xpath).click()
            else:
                self.driver.find_element("xpath", self.select_title_mr_xpath).click()
            self.driver.find_element("xpath", self.user_password_xpath).send_keys(userdata['Password'])
            date_of_birth = userdata['Date of Birth']
            day, month, year = date_of_birth.split('-')
            self.driver.find_element("xpath", self.select_day_dropdown_xpath).send_keys(day)
            self.driver.find_element("xpath", self.select_month_dropdown_xpath).send_keys(month)
            self.driver.find_element("xpath", self.select_year_dropdown_xpath).send_keys(year)
            self.driver.find_element("xpath", self.first_name_xpath).send_keys(userdata['FirstName'])
            self.driver.find_element("xpath", self.last_name_xpath).send_keys(userdata['LastName'])
            self.driver.find_element("xpath", self.company_name_xpath).send_keys(userdata['CompanyName'])
            self.driver.find_element("xpath", self.address_1_xpath).send_keys(userdata['Address1'])
            self.driver.find_element("xpath", self.address_2_xpath).send_keys(userdata['Address2'])
            country = userdata['Country']
            self.driver.find_element("xpath", self.select_country_dropdown_xpath).send_keys(country)
            self.driver.find_element("xpath", self.state_xpath).send_keys(userdata['State'])
            self.driver.find_element("xpath", self.city_xpath).send_keys(userdata['City'])
            self.driver.find_element("xpath", self.zip_code_xpath).send_keys(userdata['ZipCode'])
            self.driver.find_element("xpath", self.mobile_number_xpath).send_keys(userdata['MobileNumber'])
            self.driver.find_element("xpath", self.create_button_xpath).click()
            self.driver.find_element("xpath", self.continue_button_xpath).click()
