from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.get("https://bookcart.azurewebsites.net/register")
driver.implicitly_wait(3)

try:
    print("Login form loaded.")
    
    # Isi form registrasi
    driver.find_element(By.XPATH, "//input[@formcontrolname='firstName']").send_keys("bagas")
    driver.find_element(By.XPATH, "//input[@formcontrolname='lastName']").send_keys("bimaziz")
    driver.find_element(By.XPATH, "//input[@formcontrolname='userName']").send_keys("Bagas123")
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("Bagas123")
    driver.find_element(By.XPATH, "//input[@formcontrolname='confirmPassword']").send_keys("Bagas123")
    driver.find_element(By.XPATH, "//input[@id='mat-radio-0-input']").click() #memilih radio button male
    driver.find_element(By.XPATH,"//button[@class='mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']//span[@class='mat-mdc-button-touch-target']").click() #Mohon maaf saya stuck disini karena selector pada submit registernya salah terus, waktu explore jga ga cukup

    print("Form submitted.")
    driver.implicitly_wait(2)
    
    print("Waiting for success message...")
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mat-simple-snackbar"))
    ).text
    print("Registration Success Message:", success_message)
    
    expected_url = "https://bookcart.azurewebsites.net/login"
    assert driver.current_url == expected_url, f"URL tidak sesuai. Expected URL: {expected_url}, Current URL: {driver.current_url}"

    print("Register success")

finally:
    print("Closing browser...")
    driver.quit()