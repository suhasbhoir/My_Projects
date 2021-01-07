import datetime as dt 
import pyttsx3 as py3
import speech_recognition as sr 
import wikipedia as wiki
import webbrowser as wb
import os 
import subprocess as sp
import random as rd
import weather_forecast as wf
import requests as rq
from PIL import Image as img
import pywhatkit as kit
import pyjokes
import json
import pyautogui
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# class Jarvis:
def speakJarv(audio):
    engine = py3.init()
    voices = engine.getProperty('voices') 
    volume = engine.getProperty('volume')
    engine.setProperty('rate', 135)
    engine.setProperty('volume',1.0)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def wishJarv():
    hour = int(dt.datetime.now().hour)
    if 0 <= hour <= 12:
        time_now = dt.datetime.now().strftime("%I:%M %p")
        speakJarv("Good Morning")
        speakJarv(f"it's {time_now}")
        speakJarv("myself Jarvis. How may i help you")
    elif 12 <= hour <= 15:
        time_now = dt.datetime.now().strftime("%I:%M %p")
        speakJarv("Good afternoon")
        speakJarv(f"it's {time_now}")
        speakJarv("myself Jarvis. How may i help you")
    elif 15 <= hour <= 21:
        time_now = dt.datetime.now().strftime("%I:%M %p")
        speakJarv("Good evening")
        speakJarv(f"it's {time_now}")
        speakJarv("myself Jarvis. How may i help you")
    else:
        time_now = dt.datetime.now().strftime("%I:%M %p")
        speakJarv("Good Night")
        speakJarv(f"it's {time_now}")
        speakJarv("myself Jarvis. How may i help you")
def myPython():
    sp.Popen(["python3 My_Projects\ADV_CALC_ini.py"])        

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
    except sr.RequestError:
        print('Please Say That Again...')
        return "None"
    except sr.UnknownValueError:
        print('Please Say That Again...')
        return "None"
    except sr.WaitTimeoutError:
        print('Please Say That Again...')
        return "None"
    return query

def workJars():
    wishJarv()
    while True:
        query = listenJarv()

        if 'how are you doing' in query:
            speakJarv("I am good")

        elif 'who are you' in query:
            speakJarv(
                "i am a fictional artificial intelligence that first appeared in the Marvel Cinematic Universe where he was voiced by Paul Bettany in Iron Man1 and Iron Man 2")

        elif 'open youtube' in query:
            wb.open("youtube.com")
            speakJarv("yes i am opening youtube for you")
            ptint("Youtube is being open........")

        elif 'open wikipedia' in query:
            wb.open("en.wikipedia.org")
            speakJarv("yes i am opening wikipedia for you")
            ptint("Wikipedia is being open........")

        elif 'time' in query:
            timenow = dt.datetime.now().strftime("%I:%M %p")
            print(timenow)
            speakJarv(f"it's {timenow}")

        elif 'date' in query:
            today = dt.datetime.now().strftime("%A %d:%B:%Y")
            print(today)
            speakJarv(f"it's {today}")

        elif 'open code' in query:
            opencode = 'C:\\Users\\Suhas Bhoir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(opencode)

        elif 'close code' in query:
            os.system("taskkill /f /im Code.exe")
            speakJarv("Closing VS code")
            print("VS code is being closed........")

        elif 'open pycharm' in query:
            opencharm = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe'
            os.startfile(opencharm)
            speakJarv("Yes, I am opening pychaarm IDE...")

        elif 'close pycharm' in query:
            os.system("taskkill /f /im pycharm64.exe")
            speakJarv("Closing pycharm IDE...")
            print("VS code is being closed........")

        elif 'open git bash' in query:
            open_git = 'C:\\Program Files\\Git\\git-bash.exe'
            os.startfile(open_git)
            speakJarv("Opening git bash")

        elif 'close git bash' in query:
            os.system("taskkill /f /im mintty.exe")
            speakJarv("Closing git bash")

        elif 'open outlook' in query:
            open_outlook = "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(open_outlook)
            speakJarv("Opening outlook mail client...")

        elif 'close outlook' in query:
            os.system("taskkill /f /im OUTLOOK.EXE")
            speakJarv("Closing outlook mail client...")

        elif 'open chrome' in query:
            openchrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(openchrome)
            speakJarv("Opening Google chrome web browser...")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
            speakJarv("Closing Google chrome web browser...")

        elif 'open ms paint' in query:
            open_msp = "C:\\WINDOWS\\system32\\mspaint.exe"
            os.startfile(open_msp)
            speakJarv("Opening microsoft paint for you...")

        elif 'close ms paint' in query:
            os.system("taskkill /f /im mspaint.exe")
            speakJarv("Closing microsoft paint...")

        elif 'close internet explorer' in query:
            os.system("taskkill /f /im iexplorer.exe")
            speakJarv("Closing internet explorer web browser...")

        elif 'close edge explorer' in query:
            os.system("taskkill /f /im msedge.exe")
            speakJarv("Closing eadge web browser...")

        elif 'play' in query:
            cont = query.replace('play', '')
            speakJarv(f"playing {cont}")
            kit.playonyt(cont)

        elif 'search' in query:
            cont = query.replace('search', '')
            kit.search(cont)
            speakJarv(f"searching {cont}")
            print(f'Searching {cont}')

        elif 'joke' in query:
            speakJarv(pyjokes.get_joke())

        elif 'who is the' in query:
            try:
                obj = query.replace('who is the', '')
                info = wiki.summary(obj)
                print(info, 2)
                speakJarv(info)
            except wiki.exceptions.DisambiguationError as e:
                speakJarv(f"whatever you ask is not match or not in wikipedia database, {e}")
                print(f"whatever you ask is not match or not in wikipedia database, {e}")
            except wiki.exceptions.PageError as pe:
                speakJarv("Requested page not found please say clear or search different result, {pe}")
                print("Requested page not found please say clear or search different result, {pe}")
            except wiki.exceptions.HTTPTimeoutError as h:
                speakJarv("{h}")
                print("{h}")
            except wiki.exceptions.RedirectError as r:
                speakJarv("{r}")
                print(f"{r}")
            except wiki.exceptions.WikipediaException as w:
                speakJarv(f"{w}")
                print(f"{w}")

        elif 'what is the' in query:
            try:
                obj = query.replace('what is the', '')
                info = wiki.summary(obj)
                print(info, 2)
                speakJarv(info)
            except wiki.exceptions.DisambiguationError as e:
                speakJarv(f"whatever you ask is not match or not in wikipedia database, {e}")
                print(f"whatever you ask is not match or not in wikipedia database, {e}")
            except wiki.exceptions.PageError as pe:
                speakJarv(f"Requested page not found please say clear or search different result, {pe}")
                print(f"Requested page not found please say clear or search different result, {pe}")
            except wiki.exceptions.HTTPTimeoutError as h:
                speakJarv(f"{h}")
                print(f"{h}")
            except wiki.exceptions.RedirectError as r:
                speakJarv(f"{r}")
                print(f"{r}")
            except wiki.exceptions.WikipediaException as w:
                speakJarv(f"{w}")
                print(f"{w}")

        elif 'arrange webex' in query:
            open_webex = "C:\\Program Files (x86)\\Webex\\Webex\\Applications\\ptoneclk.exe"
            os.startfile(open_webex)
            speakJarv("yes, i am arranging webex for you...")

        elif 'where i am' in query:
            speakJarv("Please wait...i am checking")
            try:
                url = 'https://ipinfo.io/'
                geo_req = rq.get(url)
                geo_data = geo_req.json()
                city = geo_data['city']
                region = geo_data['region']
                country = geo_data['country']
                if 'IN' in country:
                    country = country.replace('IN', "India")
                speakJarv(f"we are in {city} city and state is {region} and country {country} ")
            except Exception as e:
                print(e)

        elif 'what is my ip' in query:
            speakJarv("Please wait...i am checking")
            try:
                url = 'https://ipinfo.io/'
                ip_req = rq.get(url)
                ip_data = ip_req.json()
                ip_is = ip_data['ip']
                speakJarv(f"your ip address is {ip_is}")
                print(f"your ip address is {ip_is}")
            except Exception as e:
                print(e)

        elif 'isp details' in query:
            url = 'https://ipinfo.io/'
            isp_req = rq.get(url)
            isp_data = isp_req.json()
            for k, v in isp_data.items():
                speakJarv(f"{k} : - {v}")
                print(f"{k} : - {v}")

        elif 'screenshot' in query:
            speakJarv("Hi, Please tell me the name for the screenshot file")
            name = listenJarv().lower()
            speakJarv("Please hold the screenshot for a moment. i am taking a screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speakJarv("I am done, The screenshot was saved successfully in main folder")

        elif 'send message on whatsapp' in query:
            speakJarv("Please enter the name to whom you want to send the message")
            name = input('Enter the name of user or group : ').split()
            speakJarv("Please enter the message")
            msg = input('Enter the message : ')
            speakJarv('Now a window will appear on your screen which will show you the WhatsApp QR code. '
                      'You can scan this QR code using the WhatsApp on Web function in WhatsApp.')
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get('https://web.whatsapp.com/')
            wait = WebDriverWait(driver, 600)
            for i in range(len(name)):
                msg_box = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
                msg_box.send_keys(name[i] + Keys.ENTER)

                input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                for i in range(1):
                    input_box.send_keys(msg + Keys.ENTER)
                    speakJarv('Your message sent successfully')

        elif 'bulk whatsapp' in query:
            speakJarv("Please enter the name to whom you want to send the message")
            name = input('Enter the name of user or group : ').split()
            speakJarv("Please enter the message")
            msg = input('Enter the message : ')
            speakJarv('Now a window will appear on your screen which will show you the WhatsApp QR code. '
                      'You can scan this QR code using the WhatsApp on Web function in WhatsApp.')
            time.sleep(3)
            speakJarv('Please think twice before sending bulk messages to others, this is a kind of brute force attack')
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get('https://web.whatsapp.com/')
            wait = WebDriverWait(driver, 600)
            for i in range(len(name)):
                msg_box = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
                msg_box.send_keys(name[i] + Keys.ENTER)

                input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                for i in range(100000):
                    input_box.send_keys(msg + Keys.ENTER)
                    speakJarv('Your message sent successfully')

        elif 'sleep' in query:
            speakJarv('I am going to sleep now, to wake me up say wake up jarvis')
            break


if __name__ == '__main__':
    while True:
        my_permit = listenJarv()
        if 'wake up' in my_permit:
            workJars()
        elif 'terminate' in my_permit:
            sys.exit()


            
           
           
            

            

            
               
           
      
            
            
            
            
                                                                       
    



