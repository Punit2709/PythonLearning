import requests
import json

res = requests.get('https://data.covid19india.org/v4/min/data.min.json')
data = res.text

dataJSON =  json.loads(data)
print(dataJSON["GJ"]['districts']['Ahmedabad'])