from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import time

browsers = ["chrome", "firefox", "edge"]

# Inisialisasi browser dengan looping for

for browser in browsers:
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    try:
        #buka halaman login
        driver.get('https://www.saucedemo.com')
    
        #Fitur Login
        #isi username dan password
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys('secret_sauce')
        
        #Klik tombol login
        driver.find_element(By.ID, "login-button").click()

        #Verifikasi login berhasil dengan URL assertion
        expected_url = "https://www.saucedemo.com/inventory.html"

        if driver.current_url != expected_url:
            raise AssertionError(f"URL tidak sesuai. Expected URL : {expected_url}, Current URL: {driver.current_url}")

        #print login menggunakan browser tertentu sesuai dengan urutan
        print(f"Login Berhasil with browser {browser}")

    except NoSuchElementException as e:
        print(f"Element tidak ditemukan: {e}")

    except AssertionError as e:
        print(f"Assertion Error : {e}")

    except WebDriverException as e:
        print(f"webDriver Errror: {e}")

    finally:
        driver.quit()