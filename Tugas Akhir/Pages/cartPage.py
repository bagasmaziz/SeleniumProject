from selenium.webdriver.common.by import By
from Library import get_locator, read_config
import time

class CartPage:
    
    def __init__(self, browser):
        self.browser = browser                
        # Menambahkan locator untuk add to cart     
        self.shopping_cart = get_locator("Inventory","shopping_cart")
        self.add_to_cart_button = get_locator("Inventory","add_to_cart_button")
        self.item_backpack = get_locator("Inventory","item_backpack")
        self.remove_item_button = get_locator("Inventory","remove_item_button")
        self.checkout_button = get_locator("Cart", "checkout_button")
        
        
    def click_items(self):
        self.browser.find_element(By.ID, self.item_backpack).click()

    def click_shopping_cart(self):
        self.browser.find_element(By.XPATH, self.shopping_cart).click()
    
    def add_item_to_cart(self):
        self.browser.find_element(By.ID, self.add_to_cart_button).click()

    def remove_item(self):
        self.browser.find_element(By.ID, self.remove_item_button).click()
 
    def click_checkout(self):
        self.browser.find_element(By.ID, self.checkout_button).click()
    
    
        
   
        




   