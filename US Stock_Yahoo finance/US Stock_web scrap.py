import time
from bs4 import BeautifulSoup as BeautifulSoup
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
import pandas as pd


stocks = ["INTC","AMD","TSM","UMC","ASX","AMKR","IMOS","KLIC","SNPS","CDNS","CRUS","LSCC","AMAT","ASML","LRCX","KLAC","TER","MU","TXN","ADI","AVGO","SLAB","QCOM","MRVL","NVDA","ATI","NTAP","NXPI","STM","RMBS","HPQ","IBM","BBY","A","FLEX","CLS","JBL","AAPL","NOK","ERIC","CSCO","KOPN","SWKS","T","JNPR","CIEN","LPL","GLW","FSLR","SPWR","MSFT","ORCL","ADBE","NLOK","CHKP","VRSN","CRM","DXC","SPLK","GOOG","FB","NFLX","AMZN","EBAY","BABA","BIDU","WB"]

stock_price_list = []

for i in stocks:
    url = "https://hk.finance.yahoo.com/quote/" + i +"/history?period1=1652313600&period2=1652400000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true/"
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    parsed_html = BeautifulSoup(driver.page_source, "html.parser")
    time.sleep(1)
    layer1 = parsed_html.find_all(class_="Py(10px) Pstart(10px)")
    price1 = (float(layer1[0].span.get_text().replace(",", "")) + float(layer1[4].span.get_text().replace(",", ""))) / 2

    # url = "https://hk.finance.yahoo.com/quote/" + i + "/history?period1=1640563200&period2=1640649600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true/"
    # driver = webdriver.Chrome('./chromedriver')
    # driver.get(url)
    # parsed_html = BeautifulSoup(driver.page_source, "html.parser")
    # layer1 = parsed_html.find_all(class_="Py(10px) Pstart(10px)")
    # price2 = (float(layer1[0].span.get_text().replace(",", "")) + float(layer1[4].span.get_text().replace(",", ""))) / 2

    # s = [i, price1, price2, ((price2 - price1) / price1) * 100]
    s = [i, price1]
    print(s)
    stock_price_list.append(s)


print(stock_price_list)
# change stock_price_list to dataframe and then to_csv
# col_name = ["stock", "price@24/03/2020", "price@27/12/2021", "change rate"]
# df = pd.DataFrame(stock_price_list, columns=col_name)
# df.to_csv("US Stock_web scrap.csv")


######

col_name = ["stock", "price@12/05/2022"]
df = pd.DataFrame(stock_price_list, columns=col_name)
df.to_csv("US Stock_web scrap (2).csv")













