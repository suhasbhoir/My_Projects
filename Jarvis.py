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
# import ADV_CALC_ini
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
    if hour >= 0 and hour <= 12:
        timenow = dt.datetime.now().strftime("%I:%M %p")
        speakJarv("Good Monrning")
        speakJarv(f"it's {timenow}")
        speakJarv("myself Jarvis. How may i help you")
    elif hour >= 12 and hour <= 15:
        timenow = dt.datetime.now().strftime("%I:%M %p")
        speakJarv("Good afternoon")
        speakJarv(f"it's {timenow}")
        speakJarv("myself Jarvis. How may i help you")
    elif hour >= 15 and hour <= 21:
        timenow = dt.datetime.now().strftime("%I:%M %p")
        speakJarv("Good evening")
        speakJarv(f"it's {timenow}")
        speakJarv("myself Jarvis. How may i help you")
    else:
        timenow = dt.datetime.now().strftime("%I:%M %p")
        speakJarv("Good Night")
        speakJarv(f"it's {timenow}")
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


if __name__ == '__main__':
    # timenow = dt.datetime.now().strftime("%I:%M %p")
    wishJarv()
    # speakJarv(f"It's {timenow}")
    # print(timenow)
    while True:
        query = listenJarv()

        if 'how are you doing' in query:
            speakJarv("I am good")

        elif 'who are you' in query:
            speakJarv("i am a fictional artificial intelligence that first appeared in the Marvel Cinematic Universe where he was voiced by Paul Bettany in Iron Man1 and Iron Man 2")

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
            opengit = 'C:\\Program Files\\Git\\git-bash.exe'
            os.startfile(opengit)
            speakJarv("Opening git bash")  
            
        elif 'close git bash' in query:
            os.system("taskkill /f /im mintty.exe")
            speakJarv("Closing git bash")  

        elif 'open outlook' in query:
            openoutlook = "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(openoutlook)
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
                speakJarv("Requested page not found please say clear or search diffrent result, {pe}")
                print("Requested page not found please say clear or search diffrent result, {pe}")
            except wiki.exceptions.HTTPTimeoutError as h:
                speakJarv("{h}")
                print("{h}")
            except wiki.exceptions.DisambiguationError as d:
                speakJarv("{d}")
                print("{d}")
            except wiki.exceptions.RedirectError as r:
                speakJarv("{r}")
                print("{r}")
            except wiki.exceptions.WikipediaException as w:
                speakJarv("{w}")
                print("{w}")

        elif 'what is the' in query:
            try: 
                obj = query.replace('what is the', '')
                info = wiki.summary(obj)
                print(info, 2)
                speakJarv(info, 2)
            except wiki.exceptions.DisambiguationError as e:
                speakJarv(f"whatever you ask is not match or not in wikipedia database, {e}")
                print(f"whatever you ask is not match or not in wikipedia database, {e}")
            except wiki.exceptions.PageError as pe:
                speakJarv("Requested page not found please say clear or search diffrent result, {pe}")
                print("Requested page not found please say clear or search diffrent result, {pe}")
            except wiki.exceptions.HTTPTimeoutError as h:
                speakJarv("{h}")
                print("{h}")
            except wiki.exceptions.DisambiguationError as d:
                speakJarv("{d}")
                print("{d}")
            except wiki.exceptions.RedirectError as r:
                speakJarv("{r}")
                print("{r}")
            except wiki.exceptions.WikipediaException as w:
                speakJarv("{w}")
                print("{w}")
      
        elif 'calculator' in query:
            cal = "C:\\Users\\Suhas Bhoir\\Documents\\PYTHON\\My_Projects\\ADV_CALC.py"
            os.popen(cal)
            speakJarv("Opening your own calculator...")  

        elif 'arrange my webex' in query:
            openwebex = "C:\\Program Files (x86)\\Webex\\Webex\\Applications\\ptoneclk.exe"
            os.startfile(openwebex)
            speakJarv("yes, i am arranging webex for you...") 
        
        elif 'where i am' in query:
            speakJarv("Please wait...i am checking")
            try:
                ipadd = rq.get('https://.ipify.org').text
                print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo' + ipadd + '.json'
                georeq = rq.get(url)
                geodata = georeq.json()
                city = geodata['city']
                country = geodata['country']
                speakJarv(f"we are in {city} city")
            except Exception as e:
                print(e)

        elif 'take screenshot' in query:
            speakJarv("Hi, Please tell me the name for the screenshot file")
            name = listenJarv().lower()
            speakJarv("Please hold the screenshot for a moment. i am taking a screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()          
            img.save(f"{name}.png")
            speakJarv("I am done, The screenshot was saved successfully in main folder")     

            
           
           
            

            

            
               
           
      
            
            
            
            
                                                                       
    



