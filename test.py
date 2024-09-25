from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Correct the path to chromedriver
obj_ser = Service(r"C:\Program Files (x86)\chromedriver.exe")

driver = webdriver.Chrome(service=obj_ser)

# Open the website
driver.get('https://opensource-demo.orangehrmlive.com/')
print(driver.title)
time.sleep(10)