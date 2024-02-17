import json
import time
from Configration.conftest import json_data
from selenium.webdriver.chrome.options import Options
import pytest

from PageObjects.HomePageObject import HomePageObject
from PageObjects.SignUpPageObject import SignUpPageObject
from selenium import webdriver
from PageObjects.LoginPageObject import LoginPageObject
from PageObjects.ProductPageObject import ProductPageObject
from PageObjects.CartPageObject import CartPageObject
from PageObjects.CheckoutPageObject import CheckoutPageObject
from PageObjects.PaymentPageObject import PaymentPageObject


class Test_AddToCart:
    chrome_options = Options()
    extension_path = "Driver/adblock.crx"
    chrome_options.add_extension(extension_path)
    driver = webdriver.Chrome(options=chrome_options)

    baseURl = "https://automationexercise.com"
    driver.maximize_window()
    homePO = HomePageObject(driver)
    signPO = SignUpPageObject(driver)
    loginPO = LoginPageObject(driver)
    productPO = ProductPageObject(driver)
    cartPO = CartPageObject(driver)
    checkoutPO = CheckoutPageObject(driver)
    paymentPO = PaymentPageObject(driver)

    def test_001_addProductsToCart(self, json_data):
        self.driver.get(self.baseURl)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.homePO.navigateToSighUp_LoginPage()
        add_to_cart_data = json_data['AddToCartData']
        user_data = add_to_cart_data['UserData']
        self.loginPO.loginWithUsernameAndPassword(user_data['username'], user_data['password'])
        self.homePO.navigateToProductPage()
        products_data = add_to_cart_data['Products']
        for product in products_data:
            self.productPO.addToCard(product)
        time.sleep(4)

    def test_002_validateCart(self, json_data):
        self.homePO.navigateToCartPage()
        add_to_cart_data = json_data['AddToCartData']
        products_data = add_to_cart_data['Products']
        product_count = len(products_data)
        print(product_count)
        self.cartPO.validateCartSize(product_count)

        row_number = 1
        for product in products_data:
            self.cartPO.validateProductDetails(product, row_number)
            row_number = row_number + 1

    def test_003_removeProducts(self, json_data):
        products_to_remove = json_data['AddToCartData']['RemoveProducts']
        for product_name in products_to_remove:
            self.cartPO.removeProduct(product_name)
        time.sleep(4)

        products_data = json_data['AddToCartData']['Products']
        total_product_count = len(products_data)
        removed_products_count = len(products_to_remove)
        expected_product_count = total_product_count - removed_products_count
        self.cartPO.validateCartSize(expected_product_count)
        #click on proceed to chcekout button
        self.cartPO.proceedToCheckout()

    def test_004_reviewOrderAndPlaceOrder(self, json_data):
        add_to_cart_data = json_data['AddToCartData']
        user_data = add_to_cart_data['UserData']
        self.checkoutPO.verifyDeliveryAddress(user_data)
        products = add_to_cart_data['Products']
        products_to_remove = json_data['AddToCartData']['RemoveProducts']
        self.checkoutPO.verifyTotalAmount(products, products_to_remove)

        comment = add_to_cart_data['Comment']
        print(comment)
        self.checkoutPO.commentAndPlaceOrder(comment)

    def test_005_addPaymentDetailsAndConfirmOrder(self, json_data):
        add_to_cart_data = json_data['AddToCartData']
        card_detail = add_to_cart_data['CardDetail']
        self.paymentPO.enterCardDetailsAndConfirmOrder(card_detail)
        self.paymentPO.verifyConfirmationMessage()
