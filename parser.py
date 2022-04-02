from bs4 import BeautifulSoup
import requests

url = 'https://www.scimagojr.com/journalrank.php?page=1&total_size=32958'
page = requests.get(url)

print(page.status_code)