# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="40fa53cb047d4486b0e2f1cee267e9f4",
#                                                            client_secret="415a2f201b2e42ae80f9ae9f14b2c453"))

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])
###############################

import requests
from bs4 import BeautifulSoup

def getdata(url):  
    r = requests.get(url)  
    return r.text


train_name = "03391-rajgir-new-delhi-clone-special-rgd-to-ndls"

url = "https://www.railyatri.in/live-train-status/"+train_name 

htmldata=getdata(url) 
soup = BeautifulSoup(htmldata, 'html.parser') 

# print(soup)

data = [] 
for item in soup.find_all('script', type="application/ld+json"): 
	data.append(item.get_text()) 

df = pd.read_json (data[2]) 

# print(df["mainEntity"][0])

print(df["mainEntity"][0]['name']) 
print(df["mainEntity"][0]['acceptedAnswer']['text'])


