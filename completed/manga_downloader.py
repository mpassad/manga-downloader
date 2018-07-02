'''
+----------------------------------+
| MANGA DOWNLOADER V1.0            |
+----------------------------------+
AUTHOR : PASSADELLIS MICHAEL
DATE : 11/6/2018 
TIME : 03:21
'''
import sys
import time
from bs4 import BeautifulSoup
import requests
import time

# clears the console
def clear_console():
    from os import system, name
    system('cls' if name == 'nt' else 'reset')


# this prints in the screen the rules for the app
def helper():
    print('')
    print('Help')
    print('--------------------------------------------------------------------------------------------')
    print('1) Download all the chapters of a manga pass only the url of the manga')
    print('# python downloader.py <manga-url>')
    print('--------------------------------------------------------------------------------------------')
    print('2) Download from chapter-1 to a certain chapter do as the following example')
    print('# python downloader.py <manga-url> -t <chapter-number>')
    print('--------------------------------------------------------------------------------------------')
    print('3) Download from a certain chapter till the end of the manga ')
    print('# python downloader.py <manga-url> -f <chapter-number>')
    print('--------------------------------------------------------------------------------------------')
    print('4) Download from a certain chapter till the end of the manga just')
    print('# python downloader.py <manga-url> -f <from_chapter> -t <to_chapter>')
    print('')
    time.sleep(10)
    exit()


# gets as parameters the chapters from and to
def make_dirs(to_chapter, from_chapter=1):
    import os
    # /some-path/manga_list/one-piece/chapter-1
    WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
    LIBRARY_DIR = os.path.join(WORKING_DIR, 'LIBRARY')  # /manga/one-piece
    MANGA_DIR = os.path.join(LIBRARY_DIR, sys.argv[1])
    # checks if a directory exists
    if not os.path.exists(LIBRARY_DIR):
        # if not exists creates it
        os.makedirs(LIBRARY_DIR)

    if not os.path.exists(MANGA_DIR):
        os.makedirs(MANGA_DIR)
    
    return MANGA_DIR


# connects to mangareader and loads the list of the mangas
def load_manga_list():
    starting_time = time.time()
    print('Wait Searching the list...')
    link = 'https://www.mangareader.net/alphabetical'
    r = requests.get(link)  # makes a request to the link
    data = r.text  # converts the request to text
    soup = BeautifulSoup(data, 'html.parser')
    ul = soup.find_all('ul', 'series_alpha')
    # creates an object with all the categories
    main_list = soup.find_all('ul', 'series_alpha')
    li = main_list[0].findChildren()
    urls = []  # empty list

    for item in ul:  # loop to search to all the ul lists
        grandchilds = item.find_all('a')  # gets
        for item in grandchilds:
            # print(item)
            urls.append(item['href'])  # append item to list urls
            
    ending_time = time.time()
    print('Found:', str(len(urls)), 'Mangas')
    print('Time Passed: ', str(ending_time-starting_time),'seconds')

    return urls


#counts the contained chapters for the given url/manga
def count_chapters(manga_url):
    link = 'https://www.mangareader.net'+ '/'+ sys.argv[1]
    r = requests.get(link)  # makes a request to the link
    data = r.text  # converts the request to text
    soup = BeautifulSoup(data, 'html.parser')

    table = soup.find('table', {'id': 'listing'})
    children = table.findChildren()
    #print(sum)
    if len(children) > 4:
        a_tag = table.find_all('a')
        text_chapters = a_tag[-1].contents[0]
        breaker = text_chapters.split(' ')
        num_chapters = int(breaker[-1])
    else:
        num_chapters = 0

    del soup
    del data
    del r
    del link
    return num_chapters


#downloads the selected chapters
def chapter_downloader(MANGA_PATH,to_chapter=1, from_chapter=1):
    import os
    link = 'https://www.mangareader.net' + '/' + sys.argv[1]
    r = requests.get(link)  # makes a request to the link
    data = r.text  # converts the request to text
    soup = BeautifulSoup(data, 'html.parser')
    if arg_len >= 2:
        for chapter in range(from_chapter,to_chapter+1):
            link = 'https://www.mangareader.net' + '/' + sys.argv[1] + '/' + str(chapter) + '/' + '1'
            r = requests.get(link)  # makes a request to the link
            data = r.text  # converts the request to text
            soup = BeautifulSoup(data, 'html.parser')
            select_tag = soup.find('select', {'id': 'pageMenu'})

            if select_tag != None:
                children_tag = select_tag.find_all('option')
                pages = int(children_tag[-1].contents[0])
                print('Downloading: Chapter-'+str(chapter))
                print('Downloading: '+str(pages)+ '-pages')
                chapter_number_folder = 'chapter-'+str(chapter)
                CHAPTER_DIR = os.path.join(MANGA_PATH, chapter_number_folder)
                if not os.path.exists(CHAPTER_DIR):
                    # if not exists creates it
                    os.makedirs(CHAPTER_DIR)
            for page in range(1,pages+1):
                link = 'https://www.mangareader.net' + '/' + sys.argv[1] + '/' + str(chapter) + '/' + str(page)
                r = requests.get(link)  # makes a request to the link
                data = r.text  # converts the request to text
                soup = BeautifulSoup(data, 'html.parser')
                img_tag = soup.find('img', {'id': 'img'})
                source = img_tag['src']
                filename = str(chapter) + '-' + str(page) + '.jpg'
                # writes the image from link to file and saves it
                f = open(CHAPTER_DIR+'/'+filename, 'wb')
                f.write(requests.get(source).content)
                f.close()
    


####################################################
####################MAIN#############################
# EXECUTES THE CODE
clear_console()
print('MANGA DOWNLOADER V1.0')
print('----------------------------------')

# loads the arguments 
arg_len = len(sys.argv)
if arg_len == 1:
    helper()# prints the manual for the app

# all the other conditions
# if this has more than 
#-----------------------------------------------------------
manga_found = False
if arg_len >= 2:
    url = sys.argv[1]
    manga_urls = load_manga_list()
    num_chapters = count_chapters(url)
    MANGA_PATH = make_dirs(to_chapter=num_chapters, from_chapter=1)
    for i in manga_urls:
            if i == '/'+url:
                print('MANGA FOUND')
                manga_found = True
                break
    
    if arg_len == 2:
        # searching for the manga list
        if manga_found == True: 
            if num_chapters>0:
                chapter_downloader(MANGA_PATH, from_chapter=1, to_chapter=num_chapters)
        # check if the manga is found
        elif manga_found == False:
            print('MANGA NOT FOUND')
            exit()

    # here will download only a chapter of the manga
    elif arg_len==3:
        if manga_found == True:
            chapter_downloader(MANGA_PATH, from_chapter=int(sys.argv[2]), to_chapter=int(sys.argv[2]))
        else:
            exit()
    # this will download from_chapter to_chapter (1-4) or (1-9)
    elif arg_len==4:
        if manga_found == True:
            chapter_downloader(MANGA_PATH, from_chapter=int(sys.argv[2]), to_chapter=int(sys.argv[3]))
        else:
            exit()
