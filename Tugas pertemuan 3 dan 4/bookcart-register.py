from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi Cross Browser

browsers = ["chrome", "firefox", "edge"]

for browser in browsers:
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome (options=options)
        userName = "bagas1"
        namaBrowser = "Chrome"
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox (options=options)
        userName = "bagas2"
        namaBrowser = "Firefox"
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--guest")
        options.add_argument("--headless=new")
        driver = webdriver.Edge (options=options)
        userName = "bagas3"
        namaBrowser = "Edge"

try:

    #open browser
    driver.get ("https://bookcart.azurewebsites.net/") 

    assert "Book Cart" in driver.title 

    print(f"Website opened successfully in {namaBrowser}")

    driver.implicitly_wait(20)
       
    driver.find_element (By.CSS_SELECTOR, '[mattooltip="Login"]').click() 
    print("Login form loaded")

    driver.find_element (By.CSS_SELECTOR, '.mat-unthemed.mdc-button').click() 

    print("Register form loaded.")
    
    # Isi form registrasi
    driver.find_element(By.XPATH, "//input[@formcontrolname='firstName']").send_keys("bagas")
    driver.find_element(By.XPATH, "//input[@formcontrolname='lastName']").send_keys("bimaziz")
    driver.find_element(By.XPATH, "//input[@formcontrolname='userName']").send_keys(userName)
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("Bagas123")
    driver.find_element(By.XPATH, "//input[@formcontrolname='confirmPassword']").send_keys("Bagas123")
    driver.find_element(By.XPATH, "//input[@id='mat-radio-0-input']").click() #memilih radio button male


   # Tunggu maksimal 20 detik sampai tombol register di user registration bisa diklik
    register_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-card-actions//button[span[@class='mdc-button__label'][text()='Register']]")))
    register_button.click()
    driver.implicitly_wait(5)

    print("Form submitted.")
    
    
    print("Waiting for success message...")
    success_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mat-simple-snackbar"))
    ).text
    
    
    expected_url = "https://bookcart.azurewebsites.net/login"

    if driver.current_url != expected_url:
        raise AssertionError(f"URL tidak sesuai. Expected URL: {expected_url}, Current URL: {driver.current_url}. Registrasi Gagal")

    print("Registration Success Message:", success_message)

except AssertionError as e:
        print (f"Assertion Error: {e} ")

finally:
    print(f"Closing browser {namaBrowser}")
    driver.quit()