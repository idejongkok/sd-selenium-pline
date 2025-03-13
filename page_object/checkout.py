from selenium.webdriver.common.by import By
from locators.checkout import Locators
import allure

class Checkout:
    def __init__(self, driver):
        self.driver = driver

    
    def input_delivery(self):
        with allure.step(f"input delivery"): 
            self.driver.find_element(By.ID, Locators.first_name_text).send_keys('Aria')
            self.driver.find_element(By.ID, Locators.last_name_text).send_keys('Suseno')
            self.driver.find_element(By.ID, Locators.postal_code_text).send_keys('16830')
    
    def click_continue(self):
        with allure.step(f"click continue"): 
            self.driver.find_element(By.ID, Locators.continue_button).click()
    
    def get_product_name(self):
        name = self.driver.find_elements(By.XPATH, Locators.product_name_text)
        return name
    
    def get_product_price(self):
        price = self.driver.find_elements(By.XPATH, Locators.product_price_text)
        return price
    
    def click_finish(self):
        with allure.step(f"click finish"): 
            self.driver.find_element(By.ID, Locators.finish_button).click()