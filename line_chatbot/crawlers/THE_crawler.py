import os
import json
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

#THE Ranking

directory = 'rankings'
filename = 'THE_rankings.json'
current_dir = os.getcwd()
filepath = os.path.join(current_dir, '..', directory, filename)

# Create the directory if it doesn't exist
if not os.path.exists(os.path.join(current_dir, '..', directory)):
    os.makedirs(os.path.join(current_dir, '..', directory))

# Create the file if it doesn't exist
if not os.path.exists(filepath):
    with open(filepath, 'w') as file:
        file.write('[]')
    # Configure Selenium webdriver 
    driver = uc.Chrome()
    # Navigate to the webpage
    driver.get('https://www.timeshighereducation.com/world-university-rankings/2023/world-ranking#!/length/-1/sort_by/rank/sort_order/asc/cols/stats')  

    #Find all the university rows
    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'js-row')]")

    # Create a list to store the university data for THE World University Rankings
    THE_rankings = []

    for row in rows:
        try:
            # Extract the ranking
            rank = row.find_element(By.XPATH, "./td[1]").text
            # Extract the university's name
            university_name = row.find_element(By.XPATH, "./td[2]/a").text
            
            # Create a dictionary for the university data
            university_data = {
                "University": university_name,
                "Ranking": rank,
                "Source": "THE Ranking",
                "Year":"2023"
            }
            
            # Append the university data to the list
            THE_rankings.append(university_data)
        except:
            pass

    # # Close the Selenium WebDriver
    # driver.close()

    # Save THE Rankings data to a JSON file
    with open(filepath, 'w', encoding="utf-8") as file:
        json.dump(THE_rankings, file, indent=4,ensure_ascii=False)

    print(f"File saved at: {filepath}")