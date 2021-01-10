import requests

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/spelling/AutoComplete"

querystring = {"text":"do"}

headers = {
    'x-rapidapi-key': "452109b7admsh4bf0329e23bc7f5p1b78d1jsnd54cc612e43a",
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)