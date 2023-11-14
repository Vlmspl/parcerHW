import requests
from bs4 import BeautifulSoup
import lxml

url = "https://cash-backer.club/shops"

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

session = requests.Session()

for j in range(1, 6):
    print(f"------page {j}------")
    response = session.get(f"{url}?page={j}", headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_shops = soup.find_all("div", class_="card-body")
        for i in all_shops:
            shop_title = i.find("div", class_="shop-title")
            cash_back = i.find("div", class_="shop-rate")
            formatted_string = f"Магазин: {shop_title.text}, кэшбек: {cash_back.text}"
            print(formatted_string)
