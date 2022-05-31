import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
###################################
# .prettify()

# Part 0: get all elements in page 1
url = "https://hk.centanet.com/findproperty/en/list/transaction?q=5C8BuPxhTEBERkEOTF6Gg&gclid=Cj0KCQjwpcOTBhCZARIsAEAYLuWg6zK6GRGg73et4vdwcy0eVqd0E1UDaZFa01LxfscPazDx_kFaC7YaAvEhEALw_wcB"
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
parsed_html = soup(driver.page_source, "html.parser")
#

# Part 1: get all classes of "right-block row-cxt" (for flat deal info.) in page 1
filter1 = "right-block row-cxt"
# layer1 = parsed_html.find_all(class_=filter1)

pre_df = []

c = 0
while True:
    time.sleep(0.5)         # give buffer time to load the page
    driver.get(driver.current_url)  # get the current url after clicked "next" on the previous iteration
    parsed_html = soup(driver.page_source, "html.parser")  # re-do the html parsing & class searching in the current page
    layer2 = parsed_html.find_all(class_=filter1)
    time.sleep(1)
    for i in layer2:
        row = []
        class_names = ["title-lg", "adress tag-adress", "hidden-sm-and-up", "date", "price"]
                    #   address,    district,            S.A. ft,            date,   price
        for name in class_names:
            row.append(i.find(class_=name).text if i.find(class_=name) else "") # get text if the class exists, else ""
        print(row)
        pre_df.append(row)
    time.sleep(1)
    # print(pre_df[-1])
    c += 1
    print("page ", c)
    time.sleep(0.5)
    n = driver.find_element(By.CLASS_NAME,"btn-next")
    if n and c < 417:
        n.click()                   # go to the next page after scrapped the current page
    else:
        break       # stop scrapping when there's no more "next" button

print(pre_df)
# change pre_df to dataframe and then to_csv
col_name = ["address", "district", "S.A ft", "deal date", "deal price"]
df = pd.DataFrame(pre_df, columns=col_name)
df.to_csv("Centanet 417pages_web-scrap.csv")

