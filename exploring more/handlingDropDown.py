import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service(r"C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.automationtesting.co.uk/dropdown.html")
driver.maximize_window()

#drop_country = driver.find_element(By.XPATH,"//select[@id='input-country']")

drp_country = Select(driver.find_element(By.XPATH,"//select[@id='cars']"))


drp_country.select_by_value('bmw')
time.sleep(10)

#also by value you can choose::::
#drp_country.select_by_value(10)
allopt = drp_country.options
print("all options are ",len(allopt))
