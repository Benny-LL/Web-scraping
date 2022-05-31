import requests
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
###################################

# use "webdriver" in selenium to simulate browser behavior
# Pay attention to the size of the letters

browser_options = webdriver.ChromeOptions()               # modify the setting of the temp Chrome browser
# browser_options.add_argument("--headless")                # for not opening the browser (to save computer resource)
browser_options.add_experimental_option("detach",True)    # for not auto closing the browser when all code ends

s = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=s,options=browser_options)
browser.get("https://www.parknshop.com/zh-hk/")

l1 = browser.find_element(By.CSS_SELECTOR,'[data-id="m-subcategory-310100"]')
l2 = l1.find_element(By.CSS_SELECTOR,'[class="no-subcat-name"]')
# t = []

# for i in l2:
print(l2.text)
# l2.click()






# notes:
# for e in elements:
#     print(e.text)

# vars()[name] = []

# auto-upgrade


#       //*[@id="m-category-310000"]/div[2]/a/span
#       //*[@id="m-category-310000"]
#       //*[@id="home-top-promo-module"]/div[1]/div[3]/div/div[2]/div[3]
#       //*[@id="home-top-promo-module"]


#       //*[@id="m-category-300000"]/div[3]/a
#       //*[@id="m-subcategory-"]/a[1]
#       //*[@id="m-category-310000"]/div[2]/a
