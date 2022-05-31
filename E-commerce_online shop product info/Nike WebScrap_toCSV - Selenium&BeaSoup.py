url = "https://www.nike.com.hk/man/shoe/blazer/list.htm?intpromo=PETP"
# Connect to the website
import csv
import requests
from bs4 import BeautifulSoup as soup
# import the library needed for web data scraping

req = requests.get(url)
# build a name to represent an action of scraping website data via lib.requests

nike_page = soup(req.content, "html.parser")
# with BeautifulSoup and html.parser, to interpret the website data as readable html code content

shoe_list_product_list_hover = nike_page.find_all("dl",{"class":"product_list_hover"})
# print(shoe_list_product_list_hover)

info_name = [
        "list_skucode",
        "list_eng_name",
        "list_chi_name",
        "list_price",
        ]
info = []
for name in info_name:
    vars()[name] = []
    info.append(vars()[name])


for i in shoe_list_product_list_hover:
    i = i.find("span",{"class":"up"}).text
    list_eng_name.append(i)


for i in shoe_list_product_list_hover:
    i = i.find("span",{"class":"down"}).text
    list_chi_name.append(i)


for i in shoe_list_product_list_hover:
    i = i.find("dd", {"id":"priceAkindd"}).text
    list_price.append(i)


for i in shoe_list_product_list_hover:
    if i.has_attr("skucode"):
        list_skucode.append(i['skucode'])


info = list(map(list, zip(*info)))

# with open('test_web crawl.csv', 'w', newline='',encoding='utf_8_sig') as csvfile:
#   writer = csv.writer(csvfile)
#
#   writer.writerow(info_name)
#   writer.writerows(info)

print(info)