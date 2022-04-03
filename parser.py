from bs4 import BeautifulSoup
import requests

# неважная часть началась
def getDataFromURL(url: str) -> list[list[str]]:
    page = requests.get(url)
    if page.status_code != 200:
        return

    data = []
    soup = BeautifulSoup(page.text, "html.parser")
    tag = soup.tbody
    trtag = tag.findAll('tr')

    for i in trtag:
        tdtag = i.findAll('td')
        #tdtag contain 1 element
        data.append(getData(tdtag))

    return data


def getTitle(raw: list[str]) -> str:
    t = raw[1].__str__()
    t = t.split("<")
    t = t[2].split(">")
    return t[-1]

def getType(raw: list[str]) -> str:
    pass

def getSJR(raw: list[str]) -> str:
    pass

def getHIndex(raw: list[str]) -> str:
    pass

def getTotalDocs2020(raw: list[str]) -> str:
    pass

def getTotalDocs3year(raw: list[str]) -> str:
    pass

def getTotalRefs2020(raw: list[str]) -> str:
    pass

def getTotalCities3years(raw: list[str]) -> str:
    pass

def getCitableDocs3years(raw: list[str]) -> str:
    pass

def getCitiesDocs2years(raw: list[str]) -> str:
    pass

def getRefDocs2020(raw: list[str]) -> str:
    pass

# неважная часть закончилась
# важная часть началась

def getData(raw: list[str]) -> list[str]:
    '''
    Об функции написать
    '''
    filteredData = []

    filteredData.append(getTitle(raw))

    return filteredData

'''
Title, type, SJR, H index, Tolal docs(2020), Total dosc(3 years), Total refs.(2020), Total cities(3 years), Citable docs(3 years), Cities/docs(2 years), Ref/docs(2020)
1      2     3    4        5                 6                    7                  8                      9                      10                    11
'''
url = 'https://www.scimagojr.com/journalrank.php?page=1&total_size=32958'

data = getDataFromURL(url)

for i in data:
    print(i)