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