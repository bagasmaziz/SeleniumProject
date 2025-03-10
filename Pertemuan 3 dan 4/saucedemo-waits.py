from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inisialisasi WebDriver
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

# Tunggu beberapa detik
browser.implicitly_wait(0.5)

# Buka Halaman Login 
browser.get("https://www.saucedemo.com")

# Assert Browser Tittle
assert "Swag Labs" in browser.title

print("Website opened successfully")

# Fitur Login
# Isi username dan password
login_element = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
login_element.send_keys('standard_user')

#browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('secret_sauce')

# Klik tombol login
browser.find_element(By.ID, "login-button").click()

# Tunggu beberapa detik
browser.implicitly_wait(1)

# Verifikasi login berhasil dengan URL assertion
expected_url = "https://www.saucedemo.com/inventory.html"
assert browser.current_url == expected_url, f"URL tidak sesuai. Expected URL: {expected_url}, Current URL: {browser.current_url}"

print("logged in successfully")

# Pilih Product
add_to_cart_button = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_button.click()

print("Success add to cart")

#tunggu beberapa detik
browser.implicitly_wait(1)

# Verifikasi produk ditambahkan ke kerajang
cart_badge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
assert cart_badge.text == "1"

print("success to assert")

# Klik ikon keranjang
cart_icon = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()

print("Berhasil klik ikon keranjang")

# Tunggu beberapa detik
browser.implicitly_wait(1)

# Klik tombol checkout
checkout_button = browser.find_element(By.ID, "checkout")
checkout_button.click()

print("Berhasil klik checkout")
# Tunggu beberapa detik
browser.implicitly_wait(1)

# isi informasi checkout
first_name = browser.find_element(By.ID,"first-name").send_keys("Bagas")
last_name = browser.find_element(By.ID,"last-name").send_keys("Bimaziz")
zip_code = browser.find_element(By.ID,"postal-code").send_keys("123456")

# Klik tombol continue
continue_button = browser.find_element(By.ID, "continue")
continue_button.click()

print("Berhasil input data dan proses checkout")

# Tunggu beberapa detik
browser.implicitly_wait(1)

# Klik tombol Finish
finish_button = browser.find_element(By.ID,"finish")
finish_button.click()

# Tunggu beberapa detik
browser.implicitly_wait(1)

# Verifikasi checkout berhasil 
thank_you_message = browser.find_element(By.CLASS_NAME, "complete-header")
assert thank_you_message.text == "Thank you for your order!"

print("Berhasil Checkout")

# Tutup Browser
browser.quit()
