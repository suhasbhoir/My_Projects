# import socket
# import requests
# import sys, ipaddress
# import json
#
# public = 'http://httpbin.org/ip'
# ip_api = 'http://ip-api.com/json/'
#
# ip_req = requests.get(ip_api)
# ip_data = ip_req.json()
#
# print(ip_data)
#
#
# geo_req = requests.get(ip_api)
# geo_data = geo_req.json()
# city = geo_data['city']
# region = geo_data['regionName']
# country = geo_data['country']
# pincode = geo_data['zip']
# latitude = geo_data['lat']
# longitude = geo_data['lon']
# timezone = geo_data['timezone']
# print(f"we are in {city} city, state is {region}, pincode is {pincode}, time zone is {timezone}, latitude {latitude}, longitude {longitude} country {country} ")
#
###################################################################################################################

# import cv2
# import time

# print("Hi, Please tell me the name for the screenshot file")
# name = str(input('File name: ')).lower()
# print("Please hold the for a moment. i am taking a screenshot")
# time.sleep(3)
# videoCaptureObject = cv2.VideoCapture(0)
# result = True
# while result:
#     ret, frame = videoCaptureObject.read()
#     cv2.imwrite(name + ".jpg", frame)
#     result = False
# videoCaptureObject.release()
# cv2.destroyAllWindows()

# print("Hi, Please tell me the name for the screenshot file")
# name = str(input('File name: ')).lower()
# print("Please hold the for a moment. i am taking a screenshot")
# time.sleep(3)
# videoCaptureObject = cv2.VideoCapture(0)
# result = True
# while result:
#     ret, frame = videoCaptureObject.read()
#     cv2.imwrite(name + ".jpg", frame)
#     result = False
# videoCaptureObject.release()
# cv2.destroyAllWindows()
#######################################################

# num = 2
#
# for i in range(1, 11):
#     print(f"{num} {i}'ja {(num*i)}")
#     print(f"{num} x {i} = {(num*i)}")

import requests as rq
import json

api_key ='bf1099e0745f2d7eb499a388d55a8912'
city = input('city------>') #query.replace('weather status in', '')
# url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)

result = rq.get(url)
data = result.json()

longitude = data['coord']['lon']
latitude = data['coord']['lat']
climate = data['weather'][0]['main']
temperature = data['main']['temp']
temp = (temperature - 273.15)
pressure = data['main']['pressure']
humidity = data['main']['humidity']
winds = data['wind']['speed']
windd = data['wind']['deg']
name = data['name']
timezone = data['timezone']
for k, v in data.items():
    print(f"{k} : {v}")
print(longitude, latitude, temperature, pressure, name, timezone, winds, climate, temp)
suhas = '{0:.2f} °C'.format(temp)
print('temp is:- ' + suhas)


# from pygame import mixer 
# import random
# import os

# path = "E:\SuhasB19072018\Suhas Drive\MY PICS\MOTOG4\z3 backup\MP3\MARATHI"
# file = os.path.join(path, random.choice(os.listdir(path)))
# # Starting the mixer 
# mixer.init() 

# # Loading the song 
# mixer.music.load(file) 

# # Setting the volume 
# mixer.music.set_volume(0.7) 

# # Start playing the song 
# mixer.music.play() 

# # infinite loop 
# while True: 
	
# 	print("Press 'p' to pause, 'r' to resume") 
# 	print("Press 'e' to exit the program") 
# 	query = input(" ") 
	
# 	if query == 'p': 

# 		# Pausing the music 
# 		mixer.music.pause()	 
# 	elif query == 'r': 

# 		# Resuming the music 
# 		mixer.music.unpause() 
# 	elif query == 'e': 

# 		# Stop the mixer 
# 		mixer.music.stop() 
# 		break
