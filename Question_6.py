from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def get_fifth_quote(url):
    # Configuration du WebDriver Selenium
    driver = webdriver.Chrome()
    driver.get(url)

    # Attendre que les citations soient chargées
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quote"))
    )

    # Défilement et récupération des citations
    quotes_list = []
    while len(quotes_list) < 5:  # Attendre d'avoir au moins 5 citations
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Attendre que le contenu se charge

        # Analyser la page et récupérer les citations
        scroll_html = driver.page_source
        soup = BeautifulSoup(scroll_html, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        # Ajouter les nouvelles citations à la liste
        for quote in quotes:
            quote_text = quote.find("span", class_="text").text.strip()
            if quote_text not in quotes_list:
                quotes_list.append(quote_text)

    driver.quit()

    # Afficher la cinquième citation
    print(f"Cinquième citation : {quotes_list[4]}")


if __name__ == "__main__":
    target_url = "https://quotes.toscrape.com/js-delayed/page/5/"
    get_fifth_quote(target_url)

