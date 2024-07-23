import requests

def scrapeAndSave(url, path):
    r = requests.get(url)
    with open(path,'w') as f:
        f.write(r.text)
        

url = "https://ldce.ac.in/"

scrapeAndSave(url , "Web Scraping/scrapedData/ldce.html")

