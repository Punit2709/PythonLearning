import requests
from bs4 import BeautifulSoup

res = requests.get('https://en.wikipedia.org/wiki/List_of_HTTP_status_codes')
# print(len(res.text))
# print(res.pret)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify)
spans = soup.find_all('dt')

for span in spans:
    print(span.get_text())
