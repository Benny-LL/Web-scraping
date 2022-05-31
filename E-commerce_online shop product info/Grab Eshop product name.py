url = "https://www.nike.com.hk/man/shoe/blazer/list.htm?intpromo=PETP"
# Connect to the website

import requests
from bs4 import BeautifulSoup as soup
# import the library needed for web data scraping

req = requests.get(url)
# build a name to represent an action of scraping website data via lib.requests

nike_page = soup(req.content, "html.parser")

# with BeautifulSoup and html.parser, to interpret the website data as readable html code content

shoe_list_product_list_hover = nike_page.find_all("dl",{"class":"product_list_hover"})

for shoe_name_list in shoe_list_product_list_hover:
    shoe_name_list = shoe_name_list.find("span",{"class":"up"}).text

    print(shoe_name_list)
