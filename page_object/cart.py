from selenium.webdriver.common.by import By
from locators.cart import Locators
import allure

class Cart:
    def __init__(self, driver):
        self.driver = driver

    def check_products_data(self):
        with allure.step(f"check products data"): 
            product_name = self.driver.find_elements(By.XPATH, Locators.product_name_text)
            product_price = self.driver.find_elements(By.XPATH, Locators.product_price_Text)
            
            product = []
            for i in range(2):
                product.append({'name': product_name[i].text, 'price': product_price[i].text})
                
            return product
    
    def check_product_detail(self,name, price):
        with allure.step(f"check product detail of {name}"): 
            product_name = self.driver.find_element(By.XPATH, Locators.product_name_text).text
            product_price = self.driver.find_element(By.XPATH, Locators.product_price_Text).text
            
            assert product_name == name
            assert product_price == price
    
    def click_checkout(self):
        with allure.step(f"click checkout"): 
            self.driver.find_element(By.ID, Locators.checkout_button).click()
    
    