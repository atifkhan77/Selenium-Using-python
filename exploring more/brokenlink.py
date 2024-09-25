import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://cms.comsats.edu.pk/")
driver.maximize_window()

allLinks = driver.find_elements(By.TAG_NAME,'a')
count =0 

for link in allLinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url,"  is broken link")
        count+=1
    else:
        print(url," is valid link")

print("total number of broken links are ",count)
