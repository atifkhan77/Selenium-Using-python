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

time.sleep(3)

filter_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/div/div[1]')
filter_button.click()