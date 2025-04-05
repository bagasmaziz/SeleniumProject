from selenium.webdriver.common.by import By
from Library import get_locator, read_config
import time

class CheckoutPage:
    
    def __init__(self, browser):
        self.browser = browser                
        # Menambahkan locator untuk add to cart     
        self.continue_button = get_locator("Checkout", "continue_button")
        self.firstname = get_locator("Checkout", "firstname")
        self.lastname = get_locator("Checkout", "lastname")
        self.postalcode = get_locator("Checkout", "postalcode")
        self.finish_button = get_locator("Checkout", "finish_button")
        self.cancel_button = get_locator("Checkout", "cancel_button")
        self.back_home_button = get_locator("Checkout", "back_home_button")

        
    def enter_firstname(self, firstname):
        firstname_field = self.browser.find_element(By.ID, self.firstname)
        firstname_field.clear()
        firstname_field.send_keys(firstname)

    def enter_lastname(self, lastname):
        lastname_field = self.browser.find_element(By.ID, self.lastname)
        lastname_field.clear()
        lastname_field.send_keys(lastname)
    
    def enter_postalcode(self, postalcode):
        postalcode_field = self.browser.find_element(By.ID, self.postalcode)
        postalcode_field.clear()
        postalcode_field.send_keys(postalcode)

    def click_continue(self):
        self.browser.find_element(By.ID, self.continue_button).click()

    def is_checkout_successful(self):
        get_url = self.browser.current_url
        
        if '/checkout-complete.html'in get_url:
            print("Checkout successfully")
            return True
        else:
            print("Failed")
            return False

    def click_finish(self):
        self.browser.find_element(By.ID, self.finish_button).click()

    def click_cancel(self):
        self.browser.find_element(By.ID, self.cancel_button).click()
    
    def click_back_home(self):
        self.browser.find_element(By.ID, self.back_home_button).click()
    
        
   
        




   