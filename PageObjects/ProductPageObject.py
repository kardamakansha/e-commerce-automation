from selenium import webdriver
import time


class ProductPageObject:
    quantity_xpath = "//input[@id= 'quantity']"
    add_to_cart_button = "//button[@type= 'button']"
    continue_shopping_btn_xpath = "//button[contains(@class, 'btn-success')]"

    def __init__(self, driver):
        self.driver = driver

    def addToCard(self, product):
        category_xpath = "//a[normalize-space()='"+product['Category']+"']"
        self.driver.find_element("xpath", category_xpath).click()

        subcategory_xpath = "//a[text()='"+product['SubCategory']+" ']"
        element = self.driver.find_element("xpath", subcategory_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element("xpath", subcategory_xpath).click()

        view_product_xpath = "//div[@class='productinfo text-center']//p[text()='"+product['ProductName']+"']" \
                         "/ancestor::div[@class='product-image-wrapper']//a[text()='View Product']"
        # Product_name_xpath = "//p[text()= '"+product['ProductName']+"']"
        product_ele = self.driver.find_element("xpath", view_product_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", product_ele)
        self.driver.find_element("xpath", view_product_xpath).click()

        if 'Quantity' in product:
            self.driver.find_element("xpath", self.quantity_xpath).clear()
            self.driver.find_element("xpath", self.quantity_xpath).send_keys(product['Quantity'])

        self.driver.find_element("xpath", self.add_to_cart_button).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.continue_shopping_btn_xpath).click()







