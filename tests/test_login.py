from page_object.inventory import Inventory
from page_object.login import Login
import pytest
import allure

def test_login_standar_user(browser):
    login = Login(browser)
    inventory = Inventory(browser)
    
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login()
    
    with allure.step(f"Check current URL"): 
        current_url = browser.current_url
        assert current_url == 'https://www.saucedemo.com/inventory.html'
    
    with allure.step(f"Check Inventory page title"): 
        inventory_page_title = inventory.inventory_page_title()
        assert inventory_page_title == 'Swag Labs'
    

error_sample = [('locked_out_user','secret_sauce','Epic sadface: Sorry, this user has been locked out.'),
                ('standard_user','wrong','Epic sadface: Username and password do not match any user in this service'),
                ('wrong','secret_sauce','Epic sadface: Username and password do not match any user in this service'),
                ('','secret_sauce','Epic sadface: Username is required'),
                ('standard_user','','Epic sadface: Password is required')]

@pytest.mark.parametrize('username,password,error_message',error_sample) 
def test_login_error(browser,username,password,error_message):
    login = Login(browser)

    login.input_username(username)
    login.input_password(password)
    login.click_login()
    
    with allure.step(f"Check username error icon"): 
        username_error_icon = login.check_username_error_icon()
        assert username_error_icon == True
    
    with allure.step(f"Check password error icon"): 
        password_error_icon = login.check_password_error_icon()
        assert password_error_icon == True
    
    with allure.step(f"Check login error message"): 
        error = login.check_error_message()
        assert error == error_message