from bs4 import BeautifulSoup
import requests

url ="https://www.amazon.com/dp/B09YJ283M3/ref=syn_sd_onsite_desktop_214?ie=UTF8&psc=1&pd_rd_plhdr=t"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8"
}


response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-price-whole").getText()
price_as_float = float(price)
print(price)
# print(price)
