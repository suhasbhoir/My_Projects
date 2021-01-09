import requests as rq
import json

news_url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=f44475c3b7bd4767b5a62ce4fa72caf1'
get_data = rq.get(news_url)
print(get_data)
featchingData = get_data.content
readingNews = json.loads(featchingData)
for i in range(10):
    news = readingNews['articles'][i]['title']
    print("News", i+1, news)

# print(readingNews['articles'][0]['description'])
# readingData = json.loads(get_data)
# print(readingData)