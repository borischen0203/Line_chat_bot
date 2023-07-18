import os
import json
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

driver = uc.Chrome()
driver.get('https://www.shanghairanking.com/rankings/arwu/2022')
# Find the pagination button and click it repeatedly until it becomes unavailable
next_button = driver.find_element(By.XPATH, "//li[@title='下一页']//a[@class='ant-pagination-item-link']")

while next_button.is_enabled():
    try:
        rows = driver.find_elements(By.CLASS_NAME, 'univ-name')
        university_names = [row.text for row in rows]
        print(university_names)  
        next_button.click()
        next_button = driver.find_element(By.XPATH, "//li[@title='下一页']//a[@class='ant-pagination-item-link']") 
        # Wait for the next page to load
        time.sleep(1)  # Adjust the delay as needed
    except:
        break  
driver.quit()
