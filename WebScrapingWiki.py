import requests
from bs4 import BeautifulSoup
import pandas as pd


#url for the specified page to be scraped
url = "https://en.wikipedia.org/wiki/List_of_films_based_on_Marvel_Comics_publications"


#get the contents of the page
html = requests.get(url)

#parsing the html using a beautiful soup object
soup = BeautifulSoup(html.content, features='html.parser')
print(soup)

#look at actual webpage/features to get info needed to identify
#the corresponding html section

#search for the first table on the page
first_table = soup.find('table', {'class' : 'wikitable sortable'})
                                  
#print("-----------------------------------------------------------------------------------------")
#print(first_table.prettify())
#print("-----------------------------------------------------------------------------------------")

#<tr> represents a row in a table
#<th> column headers in a table
#<td> values in a table

#return all rows in the table

rows = first_table.find_all('tr')

#print first row
print(rows[1])

#empt list to store movie titles
movie_list = []

#loop through every row and extract relevang values

#<i> tags identifies movie title
#<i> tag usually marks a special item
for row in rows: 
    values = row.find_all('i')

    #loop through all the values and extract movie title
    for value in values:
        movie_list.append(value.getText())

print(movie_list)
                          
#convert list to pandas dataframe
df = pd.DataFrame(movie_list, columns=["Title"])
df.head()

#save dataframe as a csv file
df.to_csv("marvel_movie_list.csv")

