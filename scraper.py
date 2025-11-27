import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = []
for article in soup.find_all('article', class_='product_pod')[:5]:
    title = article.find('h3').find('a')['title']
    price = article.find('p', class_='price_color').text
    books.append({'Title': title, 'Price': price, 'Date': datetime.now().strftime("%Y-%m-%d")})

df = pd.DataFrame(books)
df.to_csv('data.csv', index=False)
print("Scraping Complete.")