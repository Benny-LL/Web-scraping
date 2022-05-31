import re
# from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
###################################
# .prettify()

# Part 1: get all the sub-product page links
url = "https://www.parknshop.com/zh-hk/"
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
subhtml = driver.page_source
parsed_html = soup(subhtml, "html.parser")

filter1 = "home-top-promo-module pns-revamp-font-icons pns-prev2-bootstrap"
layer1 = parsed_html.find(class_=filter1)
filter2 = "list-group tab-pane"
layer2 = layer1.find_all(class_=re.compile(filter2))    # re.compile(" any tags including this text ")
lv2 = "lv2-subcategory"
lv3 = "lv3-container subcategory-detail"

# level == "\n", if it contains nth.

sub_product_hrefs = []
for i in layer2:
    for l2 in i.find_all(class_=lv2):
        l3 = l2.find(class_=lv3)
        if l3.text == "\n":
            l2n = l2.find(class_="lv2-no-subcategory")
            h = l2n.attrs["href"]
            sub_product_hrefs.append(h)
        else:
            for e in l3:
                if e != "\n":
                    sub_product_hrefs.append(e.attrs["href"])
                else:
                    pass

# sub_product_link contains all the sub links

# Part 2: go into the sub links & click expand button & get product info.

url_root = "https://www.parknshop.com"

# for href in sub_product_hrefs:
