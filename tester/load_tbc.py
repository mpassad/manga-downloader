'''
reads only how the number of chapters in every manga
'''
from bs4 import BeautifulSoup
import requests
import sys


# base_url + manga_url
manga_url = '/boruto-naruto-next-generations'
link = 'https://www.mangareader.net'+manga_url
r = requests.get(link)  # makes a request to the link
data = r.text  # converts the request to text
bt = sys.getsizeof(data) # gets the size o data variable in bytes
print(str(bt), 'bytes') # prints the data
# makes a beautiful soup object and retrieves data from the link
soup = BeautifulSoup(data, 'html.parser') # our main object that loads the page
table = soup.find('table', {'id': 'listing'}) #loads all the content of the given object
a_tag = table.find_all('a') # finds all the a tags that contained in the table
del table # deletes and free up space in memory
text_chapters =a_tag[-1].contents[0] # gets the last a tag and reads the content of this
del a_tag # deletes the list with all the a tags
breaker = text_chapters.split(' ') # splits the content of the last a tag in a list
del text_chapters #deletes the text_chapters variable
num_chapters = int(breaker[-1]) #converts the string to int and stores it to a variable to use it later
del breaker # deletes the list that contains all the data
del soup # deletes the soup instance and free up memory
print('Number of chapters:', str(num_chapters)) # prints the number of chapters

