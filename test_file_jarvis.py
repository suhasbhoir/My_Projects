import requests as rq
import json
import pyttsx3 as py3

def speakJarv(audio):
    engine = py3.init()
    voices = engine.getProperty('voices') 
    volume = engine.getProperty('volume')
    engine.setProperty('rate', 120)
    engine.setProperty('volume',1.0)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def listenJarv():
    r = sr.Recognizer()
with sr.Microphone() as source:
    print('Listning...')
    r.pause_threshold = 1
    audio = r.listen(source)
try:
    print('recognizing...Your audio')
    query = r.recognize_google(audio, language='en-in')
    query = query.lower()
    if 'jarvis' in query:
        query = query.replace('jarvis', '')
        print(f'Youe said... {query}')
except sr.RequestError as e:
    print('Please Say That Again...')
    return "None"
except sr.UnknownValueError as uve:
    print('Please Say That Again...')
    return "None"
except sr.AttributeError as a:
    print('Please Say That Again...')
    return "None"
return query    

# city = ().lower
def weatherjarv(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf1099e0745f2d7eb499a388d55a8912'
    featch = rq.get(url)
    data = featch.json()
    # print(data)
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

if __name__ == '__main__':

    while True:
        query = listenJarv()

        if 'what is the climate of mumbai' in query:
            query = query.replace('what is the climate of', '')
            result = mumbai.summary
            weatherjarv(result)



# print(f" Current temprature of {city} is {temp}")
# speakJarv(f" Current temprature of {city} is {temp}")
# print(f" Wind speed  is {wind_speed}")
# speakJarv(f" Wind speed  is {wind_speed}")
# print(f" latitude is {latitude}")
# speakJarv(f" latitude is {latitude}")
# print(f" longitude is {longitude}")
# speakJarv(f" longitude is {longitude}")


