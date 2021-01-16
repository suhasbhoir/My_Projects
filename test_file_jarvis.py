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

import cv2
import time

print("Hi, Please tell me the name for the screenshot file")
name = str(input('File name: ')).lower()
print("Please hold the for a moment. i am taking a screenshot")
time.sleep(3)
videoCaptureObject = cv2.VideoCapture(0)
result = True
while result:
    ret, frame = videoCaptureObject.read()
    cv2.imwrite(name + ".jpg", frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()

print("Hi, Please tell me the name for the screenshot file")
name = str(input('File name: ')).lower()
print("Please hold the for a moment. i am taking a screenshot")
time.sleep(3)
videoCaptureObject = cv2.VideoCapture(0)
result = True
while result:
    ret, frame = videoCaptureObject.read()
    cv2.imwrite(name + ".jpg", frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()