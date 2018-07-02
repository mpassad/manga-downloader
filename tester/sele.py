from selenium import webdriver
import sys

PATH_DIR = "C:/Users/Passadellis Michael/Desktop/pdf-test/manga-downloader/geckodriver.exe"
 
browser = webdriver.Firefox(executable_path=PATH_DIR)
browser.get('http://readcomiconline.to/ComicList')
browser.