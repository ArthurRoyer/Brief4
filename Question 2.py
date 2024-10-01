import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
page_number = 1

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    next_button = soup.find(class_='next')

    if next_button:
        page_number += 1
        url = f"http://quotes.toscrape.com/page/{page_number}/"
    else:
        break

print(f"Le nombre total de pages sur ce site est de : {page_number}")
