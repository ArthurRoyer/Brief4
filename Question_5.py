from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def scrape_quotes(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # Trouver la première citation
    first_quote = driver.find_element(By.CLASS_NAME, 'quote')
    quote_text = first_quote.find_element(By.CLASS_NAME, 'text').text
    quote_author = first_quote.find_element(By.CLASS_NAME, 'author').text

    # Afficher la citation
    print(f"La première citation de cette page est : {quote_text} - {quote_author}")

    # Fermer le WebDriver
    driver.quit()

if __name__ == "__main__":
    target_url = "https://quotes.toscrape.com/js/page/10/"
    scrape_quotes(target_url)
