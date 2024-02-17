import time
from selenium import webdriver



class CheckoutPageObject:

    comment_box_xpath = "//textarea[@name='message']"
    place_order_xpath = "//a[text()='Place Order']"


    def __init__(self, driver):
        self.driver = driver

    def verifyDeliveryAddress(self, user_data):
        expected_title = user_data['Title']
        expected_first_name = user_data['FirstName']
        expected_last_name = user_data['LastName']
        expected_name = expected_title + " " + expected_first_name + " " + expected_last_name
        expected_company_name = user_data['CompanyName']
        expected_address1_name = user_data['Address1']
        expected_address2_name = user_data['Address2']

        element_list = self.driver.find_elements("xpath", "//ul[@id='address_delivery']//li")
        assert element_list[1].text == expected_name
        print("Name Matched Successfully")
        assert element_list[2].text == expected_company_name
        print("Company Name Matched Successfully")
        assert element_list[3].text == expected_address1_name
        print("Address Matched Successfully")
        assert element_list[4].text == expected_address2_name
        print("Address Matched Successfully")

        expected_city_name = user_data['City']
        expected_state_name = user_data['State']
        expected_pincode = user_data['ZipCode']
        expected_address = expected_city_name + " " + expected_state_name + " " + expected_pincode
        print(expected_address)
        assert element_list[5].text == expected_address
        print("Address Matched Successfully")

        expected_country_name = user_data['Country']
        expected_mobile_number = user_data['MobileNumber']
        assert element_list[6].text == expected_country_name
        print("Country Name Matched Successfully")
        assert element_list[7].text == expected_mobile_number
        print("Mobile Number Matched Successfully")


    def verifyTotalAmount(self, products, removed_products):
        expected_grand_total = 0
        for product in products:
            if product['ProductName'] not in removed_products:
                expected_quantity = int(product['Quantity'])
                expected_price = int(product['Price'])
                expected_total_amount = expected_quantity * expected_price
                expected_grand_total = expected_grand_total + expected_total_amount

        rows = self.driver.find_elements("xpath", "//tbody//tr")
        row_count = len(rows)
        print(row_count)
        actual_grand_total_string = self.driver.find_element("xpath", f"(//tbody//tr//td//p[@class='cart_total_price'])[{row_count}]").text
        print(actual_grand_total_string)
        currency, actual_grand_total = actual_grand_total_string.split(". ")
        print(expected_grand_total)
        print(actual_grand_total)
        assert expected_grand_total == int(actual_grand_total)
        print("Price Matched Successfully On Checkout Page")

    def commentAndPlaceOrder(self, comment):
        self.driver.find_element("xpath", self.comment_box_xpath).send_keys(comment)
        self.driver.find_element("xpath", self.place_order_xpath).click()





