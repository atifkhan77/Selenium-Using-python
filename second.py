from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time




url = 'https://www.daraz.pk'

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url)
driver.maximize_window()
search_button= driver.find_element(By.XPATH,'//*[@id="q"]')
search_button.send_keys("mobile")

search_button.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(3)

# Find the first product and click on it to view details
first_product = driver.find_element(By.XPATH, '//*[@id="id-img"]')
first_product.click()

# Wait for the product page to load
#time.sleep(3)

# Add the item to the cart
#add_to_cart_button = driver.find_element(By.XPATH, '//button[@class="pdp-button pdp-button_type_text pdp-button_theme_orange pdp-button_size_large"]')
#add_to_cart_button.click()

# Wait for the cart popup to appear
#time.sleep(3)

# Proceed to checkout
#checkout_button = driver.find_element(By.XPATH, '//a[@class="btn btn-primary btn-lg btn-block"]')
#checkout_button.click()

#on_mobile = driver.find_element(By.XPATH,'//*[@id="id-img"]')
#on_mobile.click()


