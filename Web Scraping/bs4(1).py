import requests
from bs4 import BeautifulSoup
from parse import *

with open("Web Scraping/scrapedData/ldce.html", 'r+') as fp:
    html_doc = fp.read()




# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())
# print(soup.title())
# print(soup.title.string)
# print(soup.div)
# print(soup.find_all("div"))


# to print the content of anchor tag :- "<a>"
# for link in soup.find_all("a"):
#     print(link.get("href"))

# using css selector
# print(soup.select("div.divider"))
# print(soup.find_all(class_="divider"))

# geting childer of HTML tags

# for child in soup.find("li").children:
#     print(child)

# for parent in soup.find("li").parents:
#     print(parent)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++






# -------------------------------------------
# in below we are inserting (ul tag) with (2 li tag) and stroing modifeid soup in new HTML file

# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Majama"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "Nathi Majama"
# ulTag.append(liTag)


# soup.html.body.insert(0 , ulTag)
# with open("Web Scraping/scrapedData/ldce1.html", 'w+') as fp:
#     fp.write(str(soup))


# -----------------------------------------------
def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

results= soup.find_all(has_class_but_not_id)
for res in results :
    print(res,"\n\n")