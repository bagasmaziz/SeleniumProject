from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options

# Konfigurasi headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Inisialisasi WebDriver dengan headless mode
browser = webdriver.Chrome(options=options)

try:
    browser.get('https://www.saucedemo.com')
    browser.find_element(By.ID, "user-name").send_keys('standard_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()

    #Verifikasi login berhasil dengan URL assertionn
    expected_url = "https://www.saucedemo.com/inventory.html"

    if browser.current_url != expected_url:
        raise AssertionError(f"URL tidak sesuai. Expected URL : {expected_url}, Current URL: {browser.current_url}")
    
    print("Login Berhasil")

except NoSuchElementException as e:
    print(f"Element tidak ditemukan: {e}")

except AssertionError as e:
    print(f"Assertion Error : {e}")

except WebDriverException as e:
    print(f"webDriver Errror: {e}")

finally:
    browser.quit()