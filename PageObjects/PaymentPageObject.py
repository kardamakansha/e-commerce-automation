import time
from selenium import webdriver


class PaymentPageObject:
    card_name_xpath = "//input[@name='name_on_card']"
    card_number_xpath = "//input[@name='card_number']"
    cvc_number_xpath = "//input[@name='cvc']"
    month_xpath = "//input[@name='expiry_month']"
    year_xpath = "//input[@name='expiry_year']"
    pay_and_confirm_order_xpath = "//button[@id='submit']"
    order_placed_msg_xpath = "//h2[@data-qa= 'order-placed']/b"
    continue_button_xpath  = "//a[@data-qa= 'continue-button']"

    def __init__(self, driver):
        self.driver = driver

    def enterCardDetailsAndConfirmOrder(self, card_detail):
        name_on_card = card_detail['NameOnCard']
        card_number = card_detail['CardNumber']
        cvc = card_detail['CVC']
        month = card_detail['Month']
        year = card_detail['Year']
        self.driver.find_element("xpath", self.card_name_xpath).send_keys(name_on_card)
        self.driver.find_element("xpath", self.card_number_xpath).send_keys(card_number)
        self.driver.find_element("xpath", self.cvc_number_xpath).send_keys(cvc)
        self.driver.find_element("xpath", self.month_xpath).send_keys(month)
        self.driver.find_element("xpath", self.year_xpath).send_keys(year)
        self.driver.find_element("xpath", self.pay_and_confirm_order_xpath).click()

    def verifyConfirmationMessage(self):
        actual_confirmation_msg = self.driver.find_element("xpath", self.order_placed_msg_xpath).text
        expected_msg = "ORDER PLACED!"
        print(actual_confirmation_msg)
        assert expected_msg == actual_confirmation_msg
        print("Congratulations! Your order has been confirmed!")
        self.driver.find_element("xpath", self.continue_button_xpath).click()



