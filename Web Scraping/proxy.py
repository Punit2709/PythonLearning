import requests

proxie = {
    "http" : "http://scraperapi:778865e5a1b00b4c1976783fccae26e4@proxy-server.scraperapi.com:8001"  "http://httpbin.org/ip"
}

r = requests.get("https://api64.ipify.org?format=json", proxies=proxie)
print(r.json())