import unittest
from Base import InitiateDriver
from Pages import LoginPage
from Library import read_config

class TestLoginSuccess(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.driver = InitiateDriver.StartBrowser()
        self.login_page = LoginPage(self.driver)
        
        # Ambil credential dari file config
        self.username = read_config("Credentials", "username")
        self.password = read_config("Credentials", "password")
        
    def test_success_login(self):
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login()
        
        self.assertTrue(self.login_page.is_login_successfull())        
    
    @classmethod
    def tearDown(cls):
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()