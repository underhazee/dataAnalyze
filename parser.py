from turtle import width
from bs4 import BeautifulSoup
from fpdf import FPDF
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os 

# неважная часть началась
def getTitle(raw) -> str:
    t = raw[1].__str__()
    t = t.split("<")
    t = t[2].split(">")
    return t[-1].replace(',','.')


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
    Title, Type, SJR, H index, Tolal docs(2020), Total dosc(3 years), Total refs.(2020), Total cities(3 years),
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
    file.write("Title,Type,SJR,H index,Total docs(2020),Total docs(3 years),Total refs(2020),\
Total cities(3 years),Citable docs(3 years),Cities/docs(2 years),Ref/docs(2020),Country\n")

    for i in data:
        file.write(','.join(i))
        file.write('\n')
    file.close()

 
def installer_png_to_pdf(list_name_png: list[str]): 
    pdf = FPDF() 
    
    size=len(list_name_png) 
    for nom in range(size): 
        pdf.add_page() 
        pdf.image(list_name_png[nom], x = 0, y = None, w = 0, h = 0, type = '', link = '') 
     
    pdf.output('data.pdf', 'F') 
 

def deletePNG(pngList: list[str]):
    for i in pngList:
        os.remove(i)


#data = getDataFromMultiplePages(10)
#saveToCSV(data)

pngList = []

frame = pd.read_csv("data.csv")
ax = plt.gca()
frame.groupby('Country')['Title'].nunique().plot(kind='bar', color='#20C1ED', title='Total publications by country', ax=ax)
plt.savefig('TotalPublication.png')
pngList.append('TotalPublication.png')

ax.clear()
frame.groupby('Type')['Title'].nunique().plot(kind='line', title='Total types', ax=ax)
plt.savefig('TotalTypes.png')
pngList.append('TotalTypes.png')

ax.clear()
frame[['Total docs(2020)','H index']].plot(kind='scatter', x='H index', y='Total docs(2020)', title='Total docs(2020) to H index', color='#20C1ED', ax=ax)
plt.savefig('Total docs(2020) to H index.png')
pngList.append('Total docs(2020) to H index.png')

ax.clear()
frame[['Total docs(3 years)','H index']].plot(kind='scatter', x='H index', y='Total docs(3 years)', title='Total docs(3 years) to H index', color='#20C1ED', ax=ax)
plt.savefig('Total docs(3 years) to H index.png')
pngList.append('Total docs(3 years) to H index.png')

installer_png_to_pdf(pngList)
#deletePNG(pngList)