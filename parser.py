from bs4 import BeautifulSoup
import requests

url = 'https://www.scimagojr.com/journalrank.php?page=1&total_size=32958'
page = requests.get(url)

print(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")
all = []

tag = soup.tbody

all = tag.findAll('tr')

for i in all:
    alltd = i.findAll('td')
    for j in alltd:
        print(j)
    print("\n")