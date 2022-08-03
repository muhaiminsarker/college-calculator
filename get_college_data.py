from bs4 import BeautifulSoup
from urllib.request import urlopen
import re 
import pandas as pd

#Before we can even think about outputting getting SAT score ranges for universities,  
# we have to get the list of all colleges/universities in the United States

#This data will be obtained from this website: https://www.4icu.org/us/a-z/
url = "https://www.4icu.org/us/a-z/"

#Read in the url and obtain the table data in Pandas Dataframe form
college_data = pd.read_html(url)[0]

#Rename the columns (the column names that you get from the website is lengthy)
college_data.columns = ["Rank", "University", "Town"]

#Drop the last row as it is useless
college_data = college_data[:-1]


def get_uni_names():
    """
    Returns a list with the names of all the college/universities in the US 
    """
    #Open the page
    page = urlopen(url)
    #Read the HTML in the page
    html = page.read().decode("utf-8")

    #Create BeautifulSoup object and assign it to a soup variable
    soup = BeautifulSoup(html, "html.parser")

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

def add_state_of_town(df):
    """
    Changes the Town column to show the state that the college is in

    Example: Within the Town column, San Francisco is the city or town
    that the Academy of Art University is in. 

    For that data point, it would be changed to be such that it is now
    San Francisco, California 

    Parameter df: an Pandas Dataframe with college data
    Precondition: df must have a Town column 
    """
    pass