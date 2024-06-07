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

barang=[]
for a in range(10):

    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#zeus-root')))
    time.sleep(2)

    for b in range(23):
        driver.execute_script("window.scrollBy(0, 250);")
        time.sleep(1)

    driver.execute_script("window.scrollBy(50, 0);")
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for item in soup.find_all('div', class_='css-1asz3by'):
        namaProduk      = item.find('div', class_='prd_link-product-name css-3um8ox').text
        hargaProduk     = item.find('div', class_='prd_link-product-price css-h66vau').text


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

        for item2 in item.find_all('div', class_='css-1rn0irl'):
            namaToko        = item.find('span', class_='prd_link-shop-name css-1kdc32b flip').text
            lokasi          = item.find('span', class_='prd_link-shop-loc css-1kdc32b flip').text

            barang.append(
            (namaToko, lokasi, namaProduk, hargaProduk, jual, rate)
            )

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']").click()
    time.sleep(3)

df = pd.DataFrame(barang, columns=['Nama Toko', 'Lokasi', 'Nama Produk', 'Harga Produk', 'Terjual', 'Rating'])
print(df)

df.to_csv('hotwil_tokped.csv', index=False)
print('File CSV telah dibuat')

driver.close()