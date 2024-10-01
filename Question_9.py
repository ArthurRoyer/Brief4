import requests
import time

def scrape_random_quote(url):
    start_time = time.time()  # Debut du timer

    response = requests.get(url)

    # Calcul du temps
    elapsed_time = time.time() - start_time

    if response.status_code == 200:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        quote = soup.find("span", class_="text").text.strip()
        print(f"Citation : {quote}")
        print(f"Il a fallu {elapsed_time:.2f} secondes pour récuperer la citation")
    else:
        print("Erreur lors de la récupération de la citation.")

if __name__ == "__main__":
    url = "https://quotes.toscrape.com/random"
    scrape_random_quote(url)
