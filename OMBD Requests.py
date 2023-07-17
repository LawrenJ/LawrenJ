import requests
import json

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/?apikey=c77258a4&"
    params = {}
    params["r"] = "json"
    params["t"] = title
   
    bapi_resp = requests.get(baseurl, params = params)
    return json.loads(bapi_resp.text)

#*
#def get_ratings(title):
#    movie = get_movie_data(title)

def format_score(movie_score):
    score = movie_score.replace(".", "").replace("/", "").replace("%","")
    return score


movie_score = "2.32321.2"
print(format_score(movie_score))


st = "abcabcabc"
pt = st.replace("a", "z").replace("b", "y").replace("c","x")

print(pt)

avatar = get_movie_data("Avatar")
#print(avatar)


keys = avatar.keys()
print(avatar['Ratings'])
for dic in avatar['Ratings']:
    print(dic['Source'] + " " + dic['Value'])

print(type(avatar['Ratings']))



#function for putting scores in same format: take first two values in score/string,
#if second index is a decimal, keep as is
