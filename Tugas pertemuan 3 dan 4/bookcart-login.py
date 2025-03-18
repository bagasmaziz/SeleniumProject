from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class BookcartLoginTest(unittest.TestCase):
    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://bookcart.azurewebsites.net/")
        self.assertIn("Home", self.driver.title)

        print("Website opened successfully in Chrome")

    def test_a_success_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[mattooltip="Login"]'))).click()
        
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Username"]'))).send_keys("bagas1")
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Password"]').send_keys("Bagas123")
        
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[span[@class="mdc-button__label"][text()="Login"]]'))).click()
        
        # Assertion
        displayed_username = wait.until(EC.visibility_of_element_located((By.XPATH, "//a//span[contains(text(), 'bagas1')]"))).text
        self.assertEqual(displayed_username, "bagas1")

        print("Login success")

    def test_b_failed_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[mattooltip="Login"]'))).click()
        
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Username"]'))).send_keys("bagas1")
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Password"]').send_keys("123")
        
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[span[@class="mdc-button__label"][text()="Login"]]'))).click()

        # Assertion
        error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-error"))).text
        self.assertIn("Invalid username or password", error_message)

        print("Login Failed")

    def tearDown(self):
        self.driver.quit()
        print("Close Browser")


if __name__ == "__main__":
    unittest.main()
