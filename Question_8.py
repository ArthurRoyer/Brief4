from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialiser le WebDriver
driver = webdriver.Chrome()

url = "https://quotes.toscrape.com/search.aspx"
driver.get(url)

# Définir un temps d'attente
wait = WebDriverWait(driver, 10)

# Attente du menu deroulant et voir les auteurs cliquables
author_dropdown = wait.until(EC.presence_of_element_located((By.ID, "author")))

# Select pour aller au menu deroulant
select_author = Select(author_dropdown)

# Sélectionner "Albert Einstein"
select_author.select_by_visible_text("Albert Einstein")

# Attendre que le dropdown des tags soit présent et cliquable
tag_dropdown = wait.until(EC.presence_of_element_located((By.ID, "tag")))

# Utiliser Select pour interagir avec le dropdown des tags
select_tag = Select(tag_dropdown)

# Sélectionner "music"
select_tag.select_by_visible_text("music")

# Attendre que le bouton de soumission soit cliquable et cliquer
submit_button = wait.until(EC.element_to_be_clickable((By.NAME, "submit_button")))
submit_button.click()

# Récupérer le contenu de la page
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extraire et afficher la citation
citation = soup.find("span", class_="content").text.strip()
print(citation)

time.sleep(2)

driver.quit()

