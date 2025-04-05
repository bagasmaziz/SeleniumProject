from selenium.webdriver.common.by import By
from Library import get_locator
import time

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        
        # Ambil locator dari element.cfg
        self.username_locator = get_locator("Login","username")
        self.password_locator = get_locator("Login","password")
        self.login_button_locator = get_locator("Login","login_button")
        
    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_locator).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(By.ID,self.password_locator).send_keys(password)
    
    def click_login(self):        
        self.driver.find_element(By.ID, self.login_button_locator).click()

    def is_login_successfull(self):
        # Verifikasi login berhasil dengan URL assertion
        get_url = self.driver.current_url
        
        if '/inventory.html'in get_url:
            print("Website logged in successfully")
            return True
        else:
            print("Failed")
            return False
        
        
        




   