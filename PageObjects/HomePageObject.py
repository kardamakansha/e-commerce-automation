class HomePageObject:

    signup_login_button_xpath = "//a[@href= '/login']"
    product_button_xpath = "//a[@href= '/products']"
    cart_button_xpath = "(//a[@href= '/view_cart'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def navigateToSighUp_LoginPage(self):
        self.driver.find_element("xpath", self.signup_login_button_xpath).click()

    def navigateToProductPage(self):
        self.driver.find_element("xpath", self.product_button_xpath).click()

    def navigateToCartPage(self):
        self.driver.find_element("xpath", self.cart_button_xpath).click()

