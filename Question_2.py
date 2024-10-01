import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "http://quotes.toscrape.com/login"
# Chemin vers le driver
driver = webdriver.Chrome()

# Ouvrir la page de connexion
driver.get(url)

# Attendre la page
wait = WebDriverWait(driver, 10)
login_field = wait.until(EC.presence_of_element_located((By.ID, "username")))

# Remplir login
login_field = driver.find_element(By.ID, "username")  # Identifier le champ login par "name" ou autre
login_field.send_keys("Koolkydz")

# Remplir mot de passe
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("OogieBoogie")

# Soumettre formulaire
password_field.send_keys(Keys.RETURN)

# Attendre pour que la page se charge (ici 3sec)
time.sleep(3)
