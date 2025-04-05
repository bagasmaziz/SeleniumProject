import unittest
from Base import InitiateDriver
from Pages.loginPage import LoginPage
from Pages.cartPage import CartPage
from Pages.checkoutPage import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class TestCheckout(unittest.TestCase):
    
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
        
        print("Success Add to Cart!!!")
        cart_page.click_checkout()

        self.assertIn('Your Information', self.browser.find_element(By.CSS_SELECTOR,'[data-test="title"]').text)
        print("Process to checkout form")

    def test_checkout(self):
        checkout_page = CheckoutPage(self.browser)
        checkout_page.enter_firstname("Bagas")
        checkout_page.enter_lastname("Bimaziz")
        checkout_page.enter_postalcode(123789)
        checkout_page.click_continue()

        self.assertIn('Overview', self.browser.find_element(By.CSS_SELECTOR,'[data-test="title"]').text)

        checkout_page.click_finish()
        checkout_page.is_checkout_successful()
        print("Berhasil checkout!")
        time.sleep(5)

        checkout_page.click_back_home()
        print("Back to Home")
        
    @classmethod   
    def tearDownClass(cls):
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    