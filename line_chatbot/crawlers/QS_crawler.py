#QS Ranking

import json
import os

import requests


directory = 'rankings'
filename = 'QS_rankings.json'
current_dir = os.getcwd()
filepath = os.path.join(current_dir, '..', directory, filename)

# Create the directory if it doesn't exist
if not os.path.exists(os.path.join(current_dir, '..', directory)):
    os.makedirs(os.path.join(current_dir, '..', directory))

# Create the file if it doesn't exist
if not os.path.exists(filepath):
    with open(filepath, 'w') as file:
        file.write('[]')

    # Send a GET request to retrieve the JSON data
    url = 'https://www.topuniversities.com/rankings/endpoint?nid=3816281&page=0&items_per_page=1422'
    response = requests.get(url)
    data = response.json()

    # Extract the desired data information
    QS_rankings = []

    for item in data['score_nodes']:
        # Decode the Unicode representation into the original language
        university_name = item['title']
        #.encode('latin-1').decode('utf-8')
        ranking = item['rank_display']
        university_data = {
            "University": university_name,
            "Ranking": ranking,
            "Source": "QS Ranking",
            "Year": "2024"
        }
        
        QS_rankings.append(university_data)

    # # Print the extracted data
    # for university in QS_rankings:
    #     print(university)

        # Save the extracted data to a JSON file
    with open(filepath, 'w', encoding="utf-8") as file:
        json.dump(QS_rankings, file, indent=4,ensure_ascii=False)
    print(f"File saved at: {filepath}")