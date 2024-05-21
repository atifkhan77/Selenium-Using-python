from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



url = 'https://www.daraz.pk'

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url)
driver.maximize_window()
login_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/form/div/div[1]/div[1]')  
login_button.click()