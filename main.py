# import time
#
# import requests
#
# key = "https://tonapi.io/v2/rates?tokens=ton&currencies=usd"
#
# # requesting data from url
# data = requests.get(key)
# data = data.json()
# print(data)
# # print(f"{data['symbol']} price is {data['price']}")
# print(f'name {"price_USD":>15} {"diff_24h":>15} {"diff_7d":>15}\n')
# while True:
#     time.sleep(1)
#     data = requests.get(key)
#     data = data.json()
#     price = data["rates"]["TON"]["prices"]["USD"]
#     print(f'TON {price:>15}\r', end='\n')
import time

from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()

    # user-agent
options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0  Safari/537.36 Edg/122.0.0.0")

    # disable webdriver mode

    # # for older ChromeDriver under version 79.0.3945.16
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option("useAutomationExtension", False)

    # for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.get("https://www.ozon.ru/highlight/rasprodazha-1405502/?category=15502&is_high_rating=t")
time.sleep(10)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'reload-button')))
driver.find_element(By.ID, "reload-button").click()
time.sleep(20)
driver.quit()