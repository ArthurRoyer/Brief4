import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"

# Initialiser le compteur de pages à 1
page_number = 1

# Boucle pour parcourir les pages
while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    next_button = soup.find(class_='next')

    # Trouver le bouton "next" pour déterminer s'il y a une page suivante
    if next_button:
        page_number += 1
        url = f"http://quotes.toscrape.com/page/{page_number}/"
    else:
        break

print(f"Le nombre total de pages sur ce site est de : {page_number}")
