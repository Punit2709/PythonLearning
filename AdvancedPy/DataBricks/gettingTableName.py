import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('url')
bearer_token = os.getenv('bearer_token')

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

body = {
    "catalog_name": "samples", 
    "schema_name": "accuweather"
}

response = requests.get(url, headers=headers, json = body)
data = response.json()

# if response.status_code == 200:
#     print(response.json())  # Successful request
# else:
#     print(f"Error {response.status_code}: {response.text}")  # Handle API errors
    
table_names = []
for item in data['tables']:
    table_names.append(item['name'])
    
print(table_names)
