from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from collections import defaultdict

def scrape_tag(url):
    # Initialisation du WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # Extraire et analyser la page HTML
    page_html = driver.page_source
    soup = BeautifulSoup(page_html, 'html.parser')

    # Compter les tags
    tags_counter = defaultdict(int)
    tags = soup.find_all('a', href=True)

    for tag in tags:
        href_value = tag['href']
        if '/tableful/tag/' in href_value:  # Vérifier si le lien correspond à un tag
            tag_text = tag.text.strip()
            tags_counter[tag_text] += 1

    if tags_counter:
        # Trouver le tag le plus utilisé
        most_used_tag = max(tags_counter, key=tags_counter.get)
        print(f"Le tag le plus répétitif est : {most_used_tag}")
    else:
        print("Aucun tag trouvé sur cette page.")

    driver.quit()

if __name__ == "__main__":
    target_url = "https://quotes.toscrape.com/tableful/"
    scrape_tag(target_url)
