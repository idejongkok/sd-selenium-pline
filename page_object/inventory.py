from selenium.webdriver.common.by import By
from locators.inventory import Locators
import allure

class Inventory:
    def __init__(self, driver):
        self.driver = driver
        
    def inventory_page_title(self):
        text = self.driver.find_element(By.XPATH, Locators.title_text).text
        return text
        
    def sort_hi_to_low(self):
        with allure.step(f"sort hi to low"): 
            self.driver.find_element(By.XPATH, Locators.sorting_button).click()
            self.driver.find_element(By.XPATH, Locators.hilo_option).click()
        
    def add_to_cart_product(self, prod_qty):
        with allure.step(f"add to cart product"): 
            products = self.driver.find_elements(By.XPATH, Locators.add_to_cart_button)
        
            for i in range(prod_qty):
                products[i].click()
            
    def add_to_cart(self,product):
        with allure.step(f"add to cart {product}"): 
            element = 'add-to-cart-'+product.lower().replace(' ','-')
            self.driver.find_element(By.ID, element).click()
        
    def click_cart(self):
        with allure.step(f"click cart"): 
            self.driver.find_element(By.XPATH, Locators.cart_icon_button).click()
        
    def go_to_about(self):
        with allure.step(f"go to about"): 
            self.driver.find_element(By.ID, Locators.burger_button).click()
            self.driver.find_element(By.ID, Locators.about_link).click()
    
    