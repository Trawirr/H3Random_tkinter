import bs4
import requests
import numpy as np
from os import listdir
from os.path import isfile, join

mypath = "heroes"
heroes = sorted([[f[6:-4], f[0]] for f in listdir(mypath) if isfile(join(mypath, f))])

f = open('hero.html', 'w')

random_hero = heroes[np.random.randint(len(heroes))][0]
print(random_hero)
page_hero = f'https://heroes.thelazy.net/index.php/{random_hero}'
print(page_hero)
page = requests.get(page_hero)
soup = bs4.BeautifulSoup(page.content, 'html.parser')
for img in soup.findAll('img'):
    img_urls = img['src']
    img_urls = img_urls.replace("/images", "https://heroes.thelazy.net/images")
    img['src'] = img_urls
for img in soup.findAll('a', href=True):
    img_urls = img['href']
    img_urls = img_urls.replace("/index", "https://heroes.thelazy.net/index")
    img['href'] = img_urls
tables = soup.findAll('table')[2]
page_txt = str(tables)

f.write(page_txt)
f.close()

f = open('heroes.txt', 'w')
for h in heroes:
    f.write(h[0] + '\n')
f.close()