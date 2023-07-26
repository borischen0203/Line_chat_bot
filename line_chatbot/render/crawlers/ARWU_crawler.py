import os
import json
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


#THE Ranking

directory = 'rankings'
filename = 'ARWU_rankings.json'
current_dir = os.getcwd()
filepath = os.path.join(current_dir, '..', directory, filename)

# Create the directory if it doesn't exist
if not os.path.exists(os.path.join(current_dir, '..', directory)):
    os.makedirs(os.path.join(current_dir, '..', directory))

# Create the file if it doesn't exist
if not os.path.exists(filepath):
    with open(filepath, 'w') as file:
        file.write('[]')
        
    driver = uc.Chrome()
    driver.get('https://www.shanghairanking.com/rankings/arwu/2022')
    # Find the pagination button and click it repeatedly until it becomes unavailable
    next_button = driver.find_element(By.XPATH, "//li[@title='下一页']//a[@class='ant-pagination-item-link']")
    ARWU_rankings = []
    while next_button.is_enabled():
        try:
            rows = driver.find_elements(By.CLASS_NAME, 'univ-name')
            university_names = [row.text for row in rows]
            rows = driver.find_elements(By.CLASS_NAME, 'ranking')
            rankings = [row.text for row in rows]
            
            for name, ranking in zip(university_names, rankings):
                ARWU_rankings.append({
                    "University": name,
                    "Ranking": ranking,
                    "Source": "ARWU Ranking",
                    "Year": "2022"
                })         
            try:            
                driver.find_element(By.CLASS_NAME, "ant-pagination-disabled.ant-pagination-next")
                break
            except:
                pass
            next_button.click()
            # Wait for the next page to load
            time.sleep(1)  # Adjust the delay as needed
        except:
            break  
    driver.quit()
    with open(filepath, 'w', encoding="utf-8") as file:
            json.dump(ARWU_rankings, file, indent=4,ensure_ascii=False)

    print(f"File saved at: {filepath}")

