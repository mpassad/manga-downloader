'''
1) takes the arguments and pass it to the search loop
2) opens the excel file with the manga list and search for the given query
3) if it finds it returns back the number of chapters 
4) and search in the mangareader.com for that specific manga
5) Downloads every page of all chapters
'''
import requests
from bs4 import BeautifulSoup
import openpyxl as excel
import sys
import os
from time import sleep

# clear screen
def clear_console():
    os.system('cls' if os.name == 'nt' else 'reset')


    
# Method that downloads every chapter 
def download_chapter(manga_url, manga_chapters):
    pass    




if manga_chapters == 0:
    print('Not Available Chapters:')
    print('please come back later')
else:
    pass

# prints message with the correct number of arguments
if(len(sys.argv) == 1):
    clear_console()
    print('MANGA DOWNLOADER V1.0')
    print('--------------------------------------------------------------------')
    print('ERROR: Not given Manga for Downloading')
    print('python image.py <manga_url> <from_chapter> <to_chapter>')
    exit()
elif(len(sys.argv) == 2):
    pass

elif(len(sys.argv) == 3):
    print('DOWNLOADING')
    print('Manga: ',str(sys.argv[1]))
    print('Chapters:', str(sys.argv[2]))

print('Do you want to Proceed?')
desicion = input("Please Select 'y' or 'n':")
if(desicion == 'y'):
    # here will go all the loop that loads the page
    if():
        pass
else:
    exit()


chapter='/1'
manga = '/one-piece'
link = 'https://www.mangareader.net'+manga+chapter # all the link
r = requests.get(link)  # makes a request to the link
data = r.text  # converts the request to text

# makes a beautiful soup object and retrieves data from the link
soup = BeautifulSoup(data, 'html.parser')
img_tag = soup.find('img',{'id':'img'})
print(img_tag['src']) # returns the link to the image

select_tag = soup.find('select', {'id':'pageMenu'})
children_tag = select_tag.find_all('option')
num_of_pages = int(children_tag[-1].contents[0])
print(num_of_pages)
print(type(num_of_pages))




# LOAD LOOP
# chapters loop
for j in range(1,manga_chapters+1):
    # pages loop
    for i in range(1,num_of_pages+1):
        link = 'https://www.mangareader.net' + url + '/' + str(j) + '/' +str(i)
        print(link)
        r = requests.get(link)  # makes a request to the link
        data = r.text  # converts the request to text
        soup = BeautifulSoup(data,'html.parser')
        img_tag = soup.find('img', {'id': 'img'})
        source = img_tag['src']
        filename = str(j)+ '-'+ str(i) + '.jpg'
        # writes the image from link to file and saves it
        f = open(filename , 'wb')
        f.write(requests.get(source).content)
        f.close()
    
