import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook

proxie = {
    "http" : "http://scraperapi:778865e5a1b00b4c1976783fccae26e4@proxy-server.scraperapi.com:8001"  "http://httpbin.org/ip"
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        
url = "https://www.flipkart.com/search?q=samsung&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

data = {"title":[], "price":[]}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text , 'html.parser')
# print(soup.prettify)

spans = soup.select("a.s1Q9rs")
# print(spans)

for span in spans:
    # print(span.get_text())
    data["title"].append(span.get_text())

prices = soup.select("div._30jeq3")

for price in prices:
    # print(price.get_text())
    data["price"].append(price.get_text())
    if (len(data["price"]) == len((data["title"]))):
        break

df = pd.DataFrame.from_dict(data)
df.to_csv("Web Scraping/ScrapedData/flipkart.csv", index=False)