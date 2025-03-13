from page_object.inventory import Inventory
from page_object.login import Login
from page_object.cart import Cart
import allure

def test_add_to_cart_saucelabs_backpack(browser):
    '''
    Automate login flow, add "Sauce Labs Backpack" to cart and verify that correct item is added to cart
    '''
    login = Login(browser)
    inventory = Inventory(browser)
    cart = Cart(browser)
    
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login()
    
    inventory.add_to_cart('Sauce Labs Backpack')
    inventory.click_cart()

    cart.check_product_detail('Sauce Labs Backpack', '$29.99')
    
def test_add_to_cart_saucelabs_fleece_jacket(browser):
    '''
    Automate login flow, add "Sauce Labs Fleece Jacket" to cart and verify that correct item is added to cart
    '''
    login = Login(browser)
    inventory = Inventory(browser)
    cart = Cart(browser)
    
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login()
    
    inventory.add_to_cart('Sauce Labs Fleece Jacket')
    inventory.click_cart()

    cart.check_product_detail('Sauce Labs Fleece Jacket', '$49.99')
    
def test_navigate_to_about(browser):
    '''
    Automate login flow, click on hamburger button (top left), navigate to 'About' and verify if it successfully navigated or not
    '''
    login = Login(browser)
    inventory = Inventory(browser)
    
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login()
    
    inventory.go_to_about()
    
    with allure.step(f"Check current URL"): 
        current_url = browser.current_url
        assert current_url == 'https://saucelabs.com/'