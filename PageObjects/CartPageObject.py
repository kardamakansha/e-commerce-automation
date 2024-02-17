import time
from selenium import webdriver



class CartPageObject:
    no_of_items_xpath = "//tr[starts-with(@id, 'product')]"
    remove_product_xpath = "//a[text()='Full Sleeves Top Cherry - Pink']//ancestor::tr//td[@class='cart_delete']//a"
    proceed_to_checkout_xpath = "//a[text()='Proceed To Checkout']"

    def __init__(self, driver):
        self.driver = driver

    def validateCartSize(self, expected_cart_size):
        products_in_cart = self.driver.find_elements("xpath", self.no_of_items_xpath)
        actual_cart_size = len(products_in_cart)
        print(actual_cart_size)
        assert actual_cart_size == expected_cart_size

    def validateProductDetails(self, product, row_number):
        expected_product_name = product['ProductName']
        actual_product_name = self.driver.find_element("xpath",
                                               f"(//tr[contains(@id, 'product')]//td[@class='cart_description']//h4//a)[{row_number}]").text
        print("Expected Name : " + expected_product_name)
        print("Actual Name : " + actual_product_name)
        assert expected_product_name == actual_product_name

        expected_category = product['Category']
        expected_subcategory = product['SubCategory']
        expected_result = expected_category + " > " + expected_subcategory

        actual_result = self.driver.find_element("xpath",
                                                       f"(//tr[contains(@id, 'product')]//td[@class='cart_description']//p)[{row_number}]").text
        print("Expected Result : " + expected_result)
        print("Actual Result : " + actual_result)
        assert expected_result == actual_result

        expected_quantity = product['Quantity']
        actual_quantity = self.driver.find_element("xpath",f"((//tr[contains(@id, 'product')])//td[@class='cart_quantity']//button)[{row_number}]").text
        print("Expected Quantity : " + expected_quantity)
        print("Actual Quantity : " + actual_quantity)
        assert expected_quantity == actual_quantity

        #price
        expected_price = product['Price']
        actual_price_string = self.driver.find_element("xpath",f"((//tr[contains(@id, 'product')])//td[@class='cart_price']//p)[{row_number}]").text
        currency, actual_price = actual_price_string.split('. ')
        print("Expected Price : " + expected_price)
        print("Actual Price : " + actual_price)
        assert expected_price == actual_price

        expected_price = product['Price']
        quantity = product['Quantity']
        expected_total_price = int(expected_price) * int(quantity)

        actual_total_price_string = self.driver.find_element("xpath",
                                                       f"((//tr[contains(@id, 'product')])//td[@class='cart_total']//p)[{row_number}]").text
        currency, actual_total_price = actual_total_price_string.split('. ')
        print("Expected Total Price : " + str(expected_total_price))
        print("Actual Total Price : " + actual_total_price)
        assert expected_total_price == int(actual_total_price)


    def removeProduct(self, product_name):
        self.driver.find_element("xpath", f"//a[text()='{product_name}']//ancestor::tr//td[@class='cart_delete']//a").click()

    def proceedToCheckout(self):
        self.driver.find_element("xpath", self.proceed_to_checkout_xpath).click()