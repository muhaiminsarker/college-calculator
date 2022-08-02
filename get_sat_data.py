from bs4 import BeautifulSoup
from urllib.request import urlopen
import re 
import pandas as pd
import requests

#Before we can even think about outputting getting SAT score ranges for universities,  
# we have to get the list of all colleges/universities in the United States

#This data will be obtained from this website: https://www.4icu.org/us/a-z/
url = "https://www.4icu.org/us/a-z/"


#Open the page
page = urlopen(url)

#Read the HTML in the page
html = page.read().decode("utf-8")

#Create BeautifulSoup object and assign it to a soup variable
soup = BeautifulSoup(html, "html.parser")

#Find all the a tags (anchor elements) with the href containing "/reviews/" in it
#These anchor elements will have the names of all the colleges I need 
university_list = soup.findAll("a", href=re.compile("/reviews/"))
#Remove final item which is not an college

university_list.pop()
for i in university_list:
    i.get_text()


