import requests
import re
from bs4 import BeautifulSoup

response = requests.get('https://en.wikinews.org/wiki/Category:Politics_and_conflicts')
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
categories = soup.findAll('div', class_="mw-category-group")
# our_string = "CDEFGHIJKL"
new_categories = categories[6:15]
pattern = re.compile('href="(.+?)"')

# Making a list with all pages containing articles
list_href = []
for obj1 in new_categories:
    href = obj1.findAll('a')
    for obj2 in href:
        search = pattern.search(str(obj2))
        list_href += [search.group(1)]

# Making a list with all articles
list_final_href = []
for obj3 in list_href:
    response = requests.get('https://en.wikinews.org/' + obj3)
    contents = response.text
    soup1 = BeautifulSoup(contents, 'html.parser')
    categories1 = soup1.find(['ul'])
    for obj4 in categories1:
        search = pattern.search(str(obj4))
        if search != None:
            list_final_href += [search.group(1)]

print(list_final_href)




