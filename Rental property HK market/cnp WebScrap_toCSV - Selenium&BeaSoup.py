import re
import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
###################################
# .prettify()

# Part 0: get all elements in page 1
url = "https://cnp.hk/eng/tranp.php?p=&0=&e=&y=&d=ALL&b=&t=L&s="
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
parsed_html = soup(driver.page_source, "html.parser")
#

# Part 1: get all col name in page 1 table
filter_col_name = "hidden-xs table table-hover"
layer = parsed_html.find(class_=filter_col_name)

col_name = []
for i in layer.tr:
    col_name.append(i.text) if i.text != "\n" else None
#

# Part 2: get all classes of haunted_sep (for flat deal info.) in page 1
filter1 = "haunted_sep"
layer1 = layer.find_all(class_=filter1)

pre_df = []
till_when = "2019-05-02"
breaker = False
while True:
    for haunted_sep in layer1:
        row = []
        for text_cen in haunted_sep:
            t = text_cen.text
            if till_when in t:      # stop the loop once arrived the date range (oldest)
                breaker = True      # *use "breaker = True" to break multi loops*
                break               # break the innermost loop (which is the 2nd for-loop)
            else:
                row.append(t) if t != "\n" else None
        if breaker:
            break                   # break the 1st for-loop
        else:
            pre_df.append(row)      # gather rows into pre_df
    if breaker:
        break                       # break the outermost loop (which is a while-loop)
    n = driver.find_element(By.LINK_TEXT, "Next")
    if n:
        n.click()                   # go to the next page after scrapped the current page
    else:
        break       # stop scrapping when there's no more "next" button
    time.sleep(0.3)  # give buffer time to load the page
    driver.get(driver.current_url)  # get the current url after clicked "next" on the previous iteration
    parsed_html = soup(driver.page_source, "html.parser") # re-do the html parsing & class searching in the current page
    layer1 = parsed_html.find_all(class_=filter1)
    time.sleep(0.4)

# change pre_df to dataframe and then to_csv
df = pd.DataFrame(pre_df, columns=col_name)
df.to_csv("cnp 3-yrs_web-scrap.csv")
