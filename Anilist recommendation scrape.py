import requests
from bs4 import BeautifulSoup

manga = ['Nisekoi', 'Fuufu-Ijou-Koibito-Miman']

url = 'https://anilist.co/manga/105011/Fuufu-Ijou-Koibito-Miman/'


info = requests.get(url).text

testDict = {}
soupify = BeautifulSoup(info, 'html.parser')
for x in soupify.find_all('div', {'class':'recommendation-card'}):
    goal = x.find('span').find('span')['aria-label']
    testDict[goal]=goal
    print(goal)



