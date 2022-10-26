from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https:/google.com")


## Encontrar Elementos

google_text = driver.find_element(By.CLASS_NAME, "MV3Tnb").text

print(google_text)

input_box = driver.find_element(By.NAME, "q")

input_box.send_keys("selenium")

input_box.send_keys(Keys.ENTER)

## Pausa de 5 segundos

import time

print('esperaremos 5 segundos' )
time.sleep(5)

## Volvemos a la home page

home_link = driver.find_element(By.ID, "logo")

home_link.click()

## Buscar

input_box = driver.find_element(By.NAME, "q")

input_box.send_keys("selenium")

input_box.send_keys(Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium")

print(link.text)

link.click()