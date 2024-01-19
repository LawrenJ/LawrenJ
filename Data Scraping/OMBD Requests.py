import requests
import json
import statistics

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

avatar = get_movie_data("Avatar")
#print(avatar)

#top five movies of actor(s) in movie(does not include initial movie)


#Rating
#Release Year
#Actors
#Language
#Runtime
#Genre
#Director
#Writer
#Country
#Awards


print(avatar.keys())
#print(avatar['Ratings'])
#for dic in avatar['Ratings']:
    #print(dic['Source'] + " " + dic['Value'])

#print(type(avatar['Ratings']))

#print(get_average_score("Avatar"))
#test_list = ["Avatar", "Iron Man", "Black Panther"]
#print(get_list_of_average_scores(test_list))
