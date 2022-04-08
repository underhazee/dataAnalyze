from bs4 import BeautifulSoup
import requests

# неважная часть началась
def getTitle(raw) -> str:
    t = raw[1].__str__()
    t = t.split("<")
    t = t[2].split(">")
    return t[-1]


def getType(raw) -> str:
    t = raw[2].__str__()
    return t[4:-5]


def getSJR(raw) -> str:
    t = raw[3].__str__()
    t = t.split(">")
    t = t[1].split("<")
    return t[0].rstrip()


def getHIndex(raw) -> str:
    t = raw[4].__str__()
    return t[4:-5]


def getTotalDocs2020(raw) -> str:
    t = raw[5].__str__()
    return t[4:-5]


def getTotalDocs3year(raw) -> str:
    t = raw[6].__str__()
    return t[4:-5]


def getTotalRefs2020(raw) -> str:
    t = raw[7].__str__()
    return t[4:-5]


def getTotalCities3years(raw) -> str:
    t = raw[8].__str__()
    return t[4:-5]


def getCitableDocs3years(raw) -> str:
    t = raw[9].__str__()
    return t[4:-5]


def getCitiesDocs2years(raw) -> str:
    t = raw[10].__str__()
    return t[4:-5]


def getRefDocs2020(raw) -> str:
    t = raw[11].__str__()
    return t[4:-5]


def getCountry(raw) -> str:
    t = raw[12].__str__()
    t = t.split('"')
    return t[1]


def getData(raw: list[str]) -> list[str]:
    '''
    Главная функция, возвращает данные в виде списка с такими елементами:
    Title, type, SJR, H index, Tolal docs(2020), Total dosc(3 years), Total refs.(2020), Total cities(3 years),
    0      1     2    3        4                 5                    6                  7
    Citable docs(3 years), Cities/docs(2 years), Ref/docs(2020), Country
    8                      9                     10               11
    '''
    filteredData = []

    filteredData.append(getTitle(raw))
    filteredData.append(getType(raw))
    filteredData.append(getSJR(raw))
    filteredData.append(getHIndex(raw))
    filteredData.append(getTotalDocs2020(raw))
    filteredData.append(getTotalDocs3year(raw))
    filteredData.append(getTotalRefs2020(raw))
    filteredData.append(getTotalCities3years(raw))
    filteredData.append(getCitableDocs3years(raw))
    filteredData.append(getCitiesDocs2years(raw))
    filteredData.append(getRefDocs2020(raw))
    filteredData.append(getCountry(raw))

    return filteredData

# неважная часть закончилась
# важная часть началась

def getDataFromURL(url: str) -> list[list[str]]:
    '''
    Get url to parse data
    '''
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


def getDataFromMultiplePages(numOfPages: int) -> list[list[str]]:
    '''
    Enter number of pages to parse(1 page = 50 rows of data)
    '''
    baseurl = ['https://www.scimagojr.com/journalrank.php?page=', '&total_size=32958']
    data = []
    for i in range(1, numOfPages + 1):
        url = baseurl[0] + str(i) + baseurl[1]
        data.extend(getDataFromURL(url))

    return data

def saveToCSV(data: list[list[str]]):
    file = open('data.csv', 'w')
    for i in data:
        file.write(','.join(i))
        file.write('\n')
    file.close()
    print("saved")

url = 'https://www.scimagojr.com/journalrank.php?page=1&total_size=32958'

data = getDataFromMultiplePages(1)

saveToCSV(data)