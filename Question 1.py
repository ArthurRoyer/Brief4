import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")