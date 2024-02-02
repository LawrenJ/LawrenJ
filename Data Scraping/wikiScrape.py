import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import numpy as np
import statistics
import json

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/?apikey=c77258a4&"
    params = {}
    params["r"] = "json"
    params["t"] = title
   
    bapi_resp = requests.get(baseurl, params = params)
    return json.loads(bapi_resp.text)


def get_movie_scores(movie_title):
    score_dic = get_movie_data(movie_title)
    inner = score_dic['Ratings']
    
    score_list = []

    for index in inner:
        score_list.append(format_score(index['Value'][:-1]))
        
    return score_list


def format_score(movie_score):
    score = movie_score.replace(".", "").replace("/", "").replace("%","")
    score = score[:2]
    return int(score)

def get_average_score(movie):
    scores = get_movie_scores(movie)
    average = round(statistics.mean(scores), 0)
    return average

def get_list_of_average_scores(list_of_movies):
    score_list = []
    for movie in list_of_movies:
        score_list.append(get_average_score(movie))
    return score_list


def get_list_of_movies(letter):
    value_lst = []
    movie_lst = []

    letter_url = "https://en.wikipedia.org/wiki/List_of_films:_{letter}".format(letter = letter.upper())
    #print("Getting list of movies from: {}".format(letter_url))
    letter_html = requests.get(letter_url)

    alphabet_soup = BeautifulSoup(letter_html.content, features = 'html.parser')

    all_movies = alphabet_soup.find_all('div', {'class': 'mw-page-container'})

    for div in all_movies:
        value_lst = div.find_all('i')

        for value in value_lst:
            movie_lst.append(value.getText())


    return movie_lst

def get_list_of_all_movies():
    
    movie_indexes = ["numbers", "A", "B", "C", "D","E", "F", "G", "H", "I", "J-K", "L", "M", "N-O", "P", "Q-R", "S", "T", "U-W", "X-Z"]

    index_lst = []

    for index in movie_indexes:
        index_lst.append(get_list_of_movies(index))


    print("Scraping Complete")
    return index_lst

#save dataframe as a csv file

#all_movies = get_list_of_all_movies()

#print("\n")
#print("Complete")
#print("\n")

#with open("out.csv", "w", newline="", encoding='utf-8') as f:
   # writer = csv.writer(f)
   # writer.writerows(all_movies)


#test = get_list_of_movies("j")[:20]
#print(test)


#score = []


#print(get_movie_data(test[18]))

#['Country'] = 'United States'

#big_list = get_list_of_all_movies()

#movie_data_list = []
#a = get_list_of_movies("A")[:20]


a =get_list_of_movies("A")

movies = []
for i in a:
    movies[0][0] = a[i]
    movies[0][1] = i


print(a)

