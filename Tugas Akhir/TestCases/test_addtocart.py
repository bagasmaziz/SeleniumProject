import unittest
from Base import InitiateDriver
from Pages.loginPage import LoginPage
from Pages.cartPage import CartPage
from Library import read_config
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestAddToCart(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.browser = InitiateDriver.StartBrowser()
        cls.login_page = LoginPage(cls.browser)  
        cls.login_page.enter_username("standard_user")
        cls.login_page.enter_password("secret_sauce")
        cls.login_page.click_login()      
        cls.login_page.is_login_successfull()

    def test_add_to_cart(self):
        cart_page = CartPage(self.browser)
        cart_page.add_item_to_cart()
        self.browser.implicitly_wait(20)
        cart_page.click_shopping_cart()
        self.assertIn("/cart.html", self.browser.current_url)
        time.sleep(5)
        print("Success Add to Cart!!!")

    def test_remove_item_cart(self):
        cart_page = CartPage(self.browser)
        cart_page.remove_item()
        time.sleep(3)
        print("Product are Removed from Cart!")

        
    @classmethod   
    def tearDownClass(cls):
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    