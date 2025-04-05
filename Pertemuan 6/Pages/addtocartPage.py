from selenium.webdriver.common.by import By
from Library import get_locator, read_config
import time

class LoginPage:
    
    def __init__(self, browser):
        self.browser = browser        
        # Ambil locator dari element.cfg
        self.username_locator = get_locator("Login","username")
        self.password_locator = get_locator("Login","password")
        self.login_button_locator = get_locator("Login","login_button")        
        # Menambahkan locator untuk logout       
        self.burger_menu_locator = get_locator("Inventory","burger_menu")
        self.logout_button_locator = get_locator("Inventory","logout_button")
        
    def click_items():
 
    
    
        
   
        




   