import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

url = 'https://www.tokopedia.com/search?st=&q=hotwheels%20premium&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource='

driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)

for item in soup.find_all('div', class_='css-1asz3by'):
    namaProduk      = item.find('div', class_='prd_link-product-name css-3um8ox').text
    hargaProduk     = item.find('div', class_='prd_link-product-price css-h66vau').text

    for item2 in item.find_all('div', class_='css-1rn0irl'):
        lokasi          = item.find('span', class_='prd_link-shop-loc css-1kdc32b flip').text
        namaToko        = item.find('span', class_='prd_link-shop-name css-1kdc32b flip').text
        print(namaToko) 
        print(lokasi)

    terjualProduk = item.find('span', class_='prd_label-integrity css-1sgek4h')
    if terjualProduk is not None and len(terjualProduk) > 0:
        jual = item.find('span', class_='prd_label-integrity css-1sgek4h').text
    else:
        jual = ''

    ratingProduk = item.find('span', class_='prd_rating-average-text css-t70v7i')
    if ratingProduk is not None and len(ratingProduk) > 0:
        rate = item.find('span', class_='prd_rating-average-text css-t70v7i').text
    else:
        rate = ''

    print(namaProduk)
    print(hargaProduk)
    print(jual)
    print(rate)
    print("=========")


driver.close()