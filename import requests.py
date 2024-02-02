import requests
from bs4 import BeautifulSoup
import pandas as pd


#url for the specified page to be scraped

url = "https://en.wikipedia.org/wiki/Category:2000s_American_films?from=H"
url2 = "https://en.wikipedia.org/wiki/List_of_films:_C"


#get the contents of the page
html = requests.get(url)
html2 = requests.get(url2)

#parsing the html using a beautiful soup object
soup = BeautifulSoup(html.content, features='html.parser')
soup2 = BeautifulSoup(html2.content, features='html.parser')

all_divs = soup2.find_all('div', {'class': 'mw-parser-output'})


c = pd.DataFrame(all_divs)
sdfsdf = c.to_csv
#print(soup2)
