#e24.14. Project - OMDB and TasteDive

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])

import requests
import json


def no_repeats(lst):
    unique_list = []
    for index in lst:
        if index not in unique_list:
            unique_list.append(index)
            
    return unique_list


def get_movies_from_tastedive(title_string):
    baseurl = "https://tastedive.com/api/similar"
    params = {}
    params["q"] = title_string
    params["type"] = 'movies'
    params["limit"] = 5
    params["k"] = "Practicing requests as data analytics student for certification project"
   
    dive_resp = requests.get(baseurl, params = params)
    return json.loads(dive_resp.text)


def extract_movie_titles(movie_list):
    inner = movie_list['Similar']['Results']
    titles = []
   
    for i in inner:
        titles.append(i['Name'])
    return titles

def get_related_titles(movie_titles):
    
    related = []
    
    for i in movie_titles:
        p = get_movies_from_tastedive(i)
        j = extract_movie_titles(p)
        for movie in j:
            related.append(movie)
    
    cleaned_list = no_repeats(related)
         
      
    return cleaned_list

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    params = {}
    params["r"] = "json"
    params["t"] = title
   
    bapi_resp = requests.get(baseurl, params = params)
    return json.loads(bapi_resp.text)


def get_movie_rating(dict_movie):
    inner = dict_movie['Ratings']
    #print(inner)
    rating = 0
    for index in inner:
        if index['Source'] == 'Rotten Tomatoes':
            rating = int(index['Value'][:-1])
            
    #print(type(rating))
    return rating 
    
def get_sorted_recommendations(movie_list):
    
    #get list of related movies
    related_list = get_related_titles(movie_list)
    
    movie_recs = {}
    
    for i in related_list:
        movie_rating = get_movie_rating(get_movie_data(i))
        movie_recs[i] = movie_rating
    
    print(movie_recs)
        
    
    movie_recs =[i[0] for i in sorted(movie_recs.items(), key=lambda item: (item[1], item[0]), reverse=True)]
    
    return movie_recs 
    

get_movie_data("Iron Man")