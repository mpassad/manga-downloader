import sys
import time
from bs4 import BeautifulSoup
import requests
import time


def load_comic_list():
    link = 'https://www.readcomics.io/comic-list'
    r = requests.get(link)  # makes a request to the link
    data = r.text  # converts the request to text
    soup = BeautifulSoup(data, 'html.parser')
    print('Connected to:',link)

    divs = soup.find_all('ul',{'class' : 'line-list'})
    url = []
    for div in divs:
        li = div.find_all('a')
        for item in li:
            url.append(item['href'])
    print(len(url))

    return url

#=====================================
#==============MAIN====================
comic_urls = load_comic_list()
print(comic_urls)