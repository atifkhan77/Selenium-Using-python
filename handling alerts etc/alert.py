import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


obj_ser = Service(r"C:\Program Files (x86)\chromedriver.exe")

driver = webdriver.Chrome(service=obj_ser)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")


driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

time.sleep(5)

alertwindow = driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("hello")
alertwindow.accept()

##for canceling wihout accepting :::
        #alertwindow.dismiss()
time.sleep(5)
