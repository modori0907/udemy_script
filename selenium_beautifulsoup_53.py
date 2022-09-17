from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

url ="https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.65065230322266%2C%22east%22%3A-122.21600569677734%2C%22south%22%3A37.6044034633095%2C%22north%22%3A37.9457853559912%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

#  class phtocardsの下にあるaタグを全て取得する
all_link_elements = soup.select(".photo-cards a")

# 物件詳細のリンクを取得する処理
all_links = []
for link in all_link_elements:
    href = link["href"]  # aタグのhref属性の値を抽出する
    # print(href) href属性だけどhttps指定がない値もある
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select(".photo-cards address")
all_addresses = [address.getText().split(" | ")[-1] for address in all_address_elements]

"""
上記区切りの検証
address = "The Emery, 4510 Hubbard St, Emeryville, CA 94608"
print(address.split(" | ")[-1])
The Emery, 4510 Hubbard St, Emeryville, CA 94608
address1 = "19th and Harrison | 1889 Harrison St, Oakland, CA"
print(address1.split(" | ")[-1])
1889 Harrison St, Oakland, CA
"""


all_price_elements = soup.select('span[data-test="property-card-price"]')
"""
これの指定の仕方がわからず調べてやった
<span data-test="property-card-price">$2,959+/mo</span>
"""

print(all_price_elements)




# https://docs.google.com/forms/d/e/1FAIpQLSeN-Cgg3HTRtI7QbjwGkAXCfevfwLv-aDJ-B2z6sMym_EfI4w/viewform?usp=sf_link