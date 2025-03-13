from selenium.webdriver.common.by import By
from locators.login import Locators
import allure

class Login:
    def __init__(self, driver):
        self.driver = driver
    
    def input_username(self, username):
        with allure.step(f"Input username with {username}"):
            self.driver.find_element(By.ID,Locators.username_input).send_keys(username)
    
    def input_password(self, password):
        with allure.step(f"Input password with {password}"):
            self.driver.find_element(By.ID,Locators.password_input).send_keys(password)
        
    def click_login(self):
        with allure.step(f"Click Login button"):    
            self.driver.find_element(By.ID,Locators.login_button).click()
    
    def check_username_error_icon(self):   
        status = self.driver.find_element(By.XPATH, Locators.username_error_icon).is_displayed()
        return status
    
    def check_password_error_icon(self):
        status = self.driver.find_element(By.XPATH, Locators.password_error_icon).is_displayed()
        return status
    
    def check_error_message(self):
        text = self.driver.find_element(By.XPATH,Locators.error_message_text).text
        return text