import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SaucedemoTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)
        self.browser.get("https://www.saucedemo.com")

    def test_success_page_title(self):
        self.assertEqual(self.browser.title, "Swag Labs")
        print("success assert")

    def test_failed_page_title(self):
        self.assertIn('Google', self.browser.title)
        print("assert failed")

    def test_success_login(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, 'user-name').send_keys("standard_user")
        browser.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys("secret_sauce")

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Tunggu beberapa detik
        browser.implicitly_wait(1)

        # Verifikasi login berhasil dengan URL assertion
        get_url = browser.current_url
        self.assertIn('/inventory.html', get_url)

        print("Website logged in successfully")

    def test_failed_login(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, 'user-name').send_keys("standard_user")
        browser.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys("wrong_password")

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Tunggu beberapa detik
        browser.implicitly_wait(1)

        # Verifikasi login failed dengan URL assertion
        error_message = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
        self.assertIn("Username and password do not match", error_message)

        print("Website logged in Failed")

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()