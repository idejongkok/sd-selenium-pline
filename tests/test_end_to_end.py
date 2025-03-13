from page_object.inventory import Inventory
from page_object.login import Login
from page_object.cart import Cart
from page_object.checkout import Checkout
import allure
    
def test_E2E(browser):
    login = Login(browser)
    inventory = Inventory(browser)
    cart = Cart(browser)
    checkout = Checkout(browser)
    
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login()
    
    with allure.step(f"Check current URL"): 
        current_url = browser.current_url
        assert current_url == 'https://www.saucedemo.com/inventory.html'
    
    inventory.sort_hi_to_low()
    inventory.add_to_cart_product(2)
    inventory.click_cart()
    
    product_list = cart.check_products_data()
    cart.click_checkout()

    checkout.input_delivery()
    checkout.click_continue()

    with allure.step(f"Check product detail on checkout page"): 
        products = checkout.get_product_name()
        prices = checkout.get_product_price()
        
        for i in range(2):
            assert products[i].text == product_list[i]['name']
            assert prices[i].text == product_list[i]['price']
        
    checkout.click_finish()