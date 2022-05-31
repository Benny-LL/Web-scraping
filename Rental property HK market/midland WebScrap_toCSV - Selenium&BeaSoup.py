from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

URL = "https://www.hkp.com.hk/en/list/transaction/Search-H-7e9171b3"
driver = webdriver.Chrome('./chromedriver')
driver.get(URL)

subhtml = driver.page_source
soup = BeautifulSoup(subhtml, "html.parser")

links = []

# layer1 = soup.find("div", class_="sc-1xa3s3j-1 hBUjWI").find("div", class_="rmc-tabs rmc-tabs-horizontal rmc-tabs-top tabs-rmc").find("div", class_="rmc-tabs-content-wrap").find("div", class_="rmc-tabs-pane-wrap rmc-tabs-pane-wrap-active").find("div", class_="difilq-3 ljLfya").find("div", class_="sc-AxjAm sc-qse4k6-0 dQWvtg")
#
#
# for i in layer1:
#     layer2 = i.find_all("div", class_="sc-AxiKw sc-1idg3qc-0 eTpZpM difilq-1 jMvNwj")
#     for i in layer2:
#         print()
print(soup.prettify())

# row = []
#
# time.sleep(4)
# for i in soup.find_all("div", class_="sc-2vbwj7-23 jRDvDR"):
#     row.append(i.find("div", class_="sc-1u6t046-1 kLojCO").text)
#     print(i.find("div", class_="sc-1u6t046-1 kLojCO").text)
#     print(i.find("div", class_="sc-1u6t046-1 kLojCO").find("div", class_="sc-1u6t046-0 iaXPKR"))
#     print(i.find("span", class_="sc-2vbwj7-2 fdjJsZ").text)
#     print(re.search('(\d+,)*\d+.', i.find("div", class_="sc-1d6dn8u-1 buFexZ").text).group(), 'sq.ft.')
#     print(re.search('\$\d+', i.find("span", class_="sc-1d6dn8u-0 kvuMBF").text).group())
#     print(re.search('\d+\/\d+\/\d+', i.find("div", class_="sc-2vbwj7-4 sc-2vbwj7-5 bbnWtK").text).group())
#     print(re.search('(\$\d+,)*\d+', i.find("span", class_="sc-hlnw2x-6 kktEPG").text).group())
#     print('---------------\n')
#
# print(row)

# scrape each page
# p = 2
# while True:
#
#     for i in soup.find_all("div", class_="sc-2vbwj7-23 jRDvDR"):
#         print(i.find("div", class_="sc-1u6t046-1 kLojCO").text)
#         print(i.find("div", class_="sc-1u6t046-1 kLojCO").find("div", class_="sc-1u6t046-0 iaXPKR").text)
#         print(i.find("span", class_="sc-2vbwj7-2 fdjJsZ").text)
#         print(re.search('(\d+,)*\d+.', i.find("div", class_="sc-1d6dn8u-1 buFexZ").text).group(), 'sq.ft.')
#         print(re.search('\$\d+', i.find("span", class_="sc-1d6dn8u-0 kvuMBF").text).group())
#         print(re.search('\d+\/\d+\/\d+', i.find("div", class_="sc-2vbwj7-4 sc-2vbwj7-5 bbnWtK").text).group())
#         print(re.search('(\$\d+,)*\d+', i.find("span", class_="sc-hlnw2x-6 kktEPG").text).group())
#         print('---------------\n')
#
#     time.sleep(3.5)
#     n = driver.find_element(By.LINK_TEXT, str(p))
#
#     if n:
#         n.click()  # go to the next page after scrapped the current page
#     else:
#         pass
#
#     p += 1
#     subhtml = driver.page_source
#     soup = BeautifulSoup(subhtml, "html.parser")

