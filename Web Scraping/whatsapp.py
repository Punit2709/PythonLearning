import requests
from bs4 import BeautifulSoup

res = requests.get("https://web.whatsapp.com/")
# print(res.text)

soup = BeautifulSoup(res.text , 'html.parser')
# print(soup.prettify())
# title = soup.find('title')
# print(title.get_text())

span = soup.find('img')
print(span)