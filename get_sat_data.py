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

soup.find_all("td")

def get_uni_names():
    """
    Returns a list with the names of all the college/universities in the US 
    """

    #Find all the a tags (anchor elements) with the href containing "/reviews/" in it
    #These anchor elements will have the names of all the colleges I need 
    uni_tag_list = soup.findAll("a", href=re.compile("/reviews/"))

    #Remove first and final item which is not an college
    uni_tag_list = uni_tag_list[1:len(uni_tag_list)-1]

    #Obtains the college name rather than the whole anchor element and
    # puts it into a separate list
    #List comprehension is used to minimize code length
    university_list = [i.get_text() for i in uni_tag_list] 

    return university_list

def get_rank():
    pass

def get_location():
    pass