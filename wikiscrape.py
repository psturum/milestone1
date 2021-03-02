import requests
import re
from bs4 import BeautifulSoup

response = requests.get('https://en.wikinews.org/wiki/Category:Politics_and_conflicts')
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
categories = soup.findAll('div', class_="mw-category-group")
our_string = "CDEFGHIJKL"
new_categories = categories[6:15]
pattern = re.compile('href="(.+?)"')

# Making a list with all pages containing articles
list_categories = []
for obj1 in new_categories:
    href = obj1.findAll('a')
    for obj2 in href:
        search = pattern.search(str(obj2))
        list_categories += [search.group(1)]

# Making a list with page-hrefs
list_page_href = []

for obj4 in list_categories:
    response1 = requests.get('https://en.wikinews.org/' + obj4)
    contents1 = response1.text
    soup1 = BeautifulSoup(contents1, 'html.parser')
    pages = soup1.findAll('div', id="mw-pages")
    if len(pages) > 0:
        pages_links = pages[0].findAll('a')
        for obj3 in pages_links:
            search = pattern.search(str(obj3))
            list_page_href += [search.group(1)]

list_dictionaries = []

for obj5 in list_page_href:
    response3 = requests.get('https://en.wikinews.org/' + obj5)
    contents3 = response3.text
    soup2 = BeautifulSoup(contents3, 'html.parser')

    #Collecting date for meta-data
    date = soup2.findAll('strong', class_="published")
    pattern1 = re.compile('title="(.+)"')
    if len(date) > 0:
        date_trimmed = pattern1.search(str(date[0]))

    #Collecting content
    content = soup2.findAll('div', id="mw-content-text")

    #Collecting number sources for meta-data
    sources = soup2.findAll('span', class_="sourceTemplate")
    number_sources = len(sources)

    page_dic = {
        "Content": content,
        "Number of sources": number_sources,
        "Date": date_trimmed.group(1)
    }

    list_dictionaries += [page_dic]








 





