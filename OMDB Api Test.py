import requests
import json

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/?apikey=c77258a4&"
    params = {}
    params["r"] = "json"
    params["t"] = title
   
    bapi_resp = requests.get(baseurl, params = params)
    return json.loads(bapi_resp.text)



avatar = get_movie_data("Avatar")
#print(avatar)

keys = avatar.keys()
print(keys)