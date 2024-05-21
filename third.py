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
search_button = driver.find_element(By.XPATH, '//*[@id="q"]')
search_button.send_keys("mobile")
search_button.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(3)

# Find the first product and click on it to view details
first_product = driver.find_element(By.XPATH, '//*[@id="id-img"]') #//[@id="id-img"]
first_product.click()

# Wait for the product page to load
time.sleep(3)

# Add the item to the cart
add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="module_add_to_cart"]/div/button[2]')
add_to_cart_button.click()

# Wait for the cart popup to appear
time.sleep(3)

#login_button= driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div/div[2]/form/div/div[2]/div[1]/button')
#login_button.click()

email_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div/div[2]/form/div/div[1]/div[1]/input')
email_button.send_keys("testing@gmail.com")
email_button.send_keys(Keys.RETURN)
time.sleep(3)

password_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div/div[2]/form/div/div[1]/div[2]/input')
password_button.send_keys("abc123")
password_button.send_keys(Keys.RETURN)
time.sleep(3)

login_button= driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div/div[2]/form/div/div[2]/div[1]/button')
login_button.click()

