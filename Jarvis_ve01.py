import datetime as dt 
import pyttsx3 as py3
import speech_recognition as sr 
import wikipedia as wiki
import webbrowser as wb
import os, sys, random, time
import subprocess as sp
import requests as rq
import pywhatkit as kit
import pyjokes
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import pyowm
import cv2
import smtplib
import ssl
from email.message import EmailMessage
from word2number import w2n
import pygame
from googleapi import google 


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
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
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
            speakJarv("i am a fictional artificial intelligence that first appeared in the Marvel Cinematic Universe "
                "where he was voiced by Paul Bettany in Iron Man1 and Iron Man 2")

        elif 'open youtube' in query:
             wb.open("youtube.com")
             speakJarv("yes, i am opening youtube for you")
             print("Youtube is being open........")

        elif 'open wikipedia' in query:
            wb.open("en.wikipedia.org")
            speakJarv("yes i am opening wikipedia for you")
            print("Wikipedia is being open........")

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
            speakJarv("Yes, I am opening VS code for you")
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
            try:
                cont = query.replace('play', '')
                speakJarv(f"playing {cont}")
                kit.playonyt(cont)
            except kit.mainfunctions.InternetException:
                print("No Internet : needs active internet connection")


        elif 'search' in query:
            try:
                cont = query.replace('search', '')
                kit.search(cont)
                speakJarv(f"searching {cont}")
                print(f'Searching {cont}')
            except kit.mainfunctions.InternetException:
                print("No Internet : needs active internet connection")

        elif 'joke' in query:
            speakJarv(pyjokes.get_joke())

        elif 'my song' in query:
            while True:
                try:
                    path = "E:\SuhasB19072018\Suhas Drive\MY PICS\MOTOG4\z3 backup\MP3\MARATHI"
                    file = os.path.join(path, random.choice(os.listdir(path)))
                    pygame.mixer.init()
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    print("Say 'pause' to pause the song, 'resume' to unpause the song") 
                    print("say 'next' to next song, 'exit'e to close player") 
                    inputcmd = listenJarv().lower() 
                    if inputcmd == 'pause song': 
                        pygame.mixer.music.pause()	 # Pausing the music
                    elif inputcmd == 'resume song': 
                        pygame.mixer.music.unpause() # Resuming the music 
                    elif inputcmd == 'next song': 
                        pygame.mixer.music.stop() # Stop the mixer 
                    elif inputcmd == 'exit player': 
                        pygame.mixer.music.stop() # Stop the mixer 
                        break    
                except pygame.error:
                    pass

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
                url = 'http://ip-api.com/json/'
                geo_req = rq.get(url)
                geo_data = geo_req.json()
                city = geo_data['city']
                region = geo_data['regionName']
                country = geo_data['country']
                pincode = geo_data['zip']
                latitude = geo_data['lat']
                longitude = geo_data['lon']
                timezone = geo_data['timezone']
                speakJarv(f"we are in {city} city, state is {region}, Pin code is {pincode}, time zone is {timezone}, "
                          f"latitude {latitude}, longitude {longitude} country {country} ")

                print(f"we are in {city} city, state is {region}, Pin code is {pincode}, time zone is {timezone}, "
                      f"latitude {latitude}, longitude {longitude} country {country} ")
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
            speakJarv("Please wait...i am checking")
            url = 'http://ip-api.com/json/'
            isp_req = rq.get(url)
            isp_data = isp_req.json()
            for k, v in isp_data.items():
                my_isp = f'{k} : {v}'
                if 'lat' in my_isp:
                    my_isp = my_isp.replace('lat', 'latitude')
                elif 'lon' in my_isp:
                    my_isp = my_isp.replace('lon', 'longitude')
                elif 'as' in my_isp:
                    my_isp = my_isp.replace('as', 'asn')
                speakJarv(my_isp)
                print(my_isp)

        elif 'advanced calculator' in query:
            try:
                calculator
            except Exception:
                pass

        elif 'screenshot' in query:
            speakJarv("Hi, Please tell me the name for the screenshot file")
            name = listenJarv().lower()
            speakJarv("Please hold the screenshot for a moment. i am taking a screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speakJarv("I am done, The screenshot was saved successfully in main folder")

        elif 'click my photo' in query:
            speakJarv("Hi, please suggest me what to name this picture")
            name = listenJarv().lower()
            speakJarv("Wait a minute, I'm taking your picture with a Front camera "
                      "please take a look here")
            time.sleep(1)
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while result:
                ret, frame = videoCaptureObject.read()
                cv2.imwrite(name + ".jpg", frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            speakJarv(f"I am done, The picture was saved successfully with name {name} in main folder")

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

        elif 'tell me top 10 news' in query:
            news_url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=f44475c3b7bd4767b5a62ce4fa72caf1'
            get_data = rq.get(news_url)
            fetching_Data = get_data.content
            readingNews = json.loads(fetching_Data)
            for i in range(10):
                news = readingNews['articles'][i]['title']
                speakJarv(news)
                print("News", i + 1, ": -", news)

        elif 'dollar to euros' in query:
            try:
                speakJarv('tell me how many doller you want to convert in euros')
                doller = float(listenJarv())
                euros = google.convert_currency(doller, "USD", "EUR")
                print (doller + " USD = {0} EUR".format(euros))
            except Exception:
                pass

        elif 'do addition' in query:
            try:
                def add(x, y):
                    z = x + y
                    return z
                speakJarv("tell me your first number")
                x = int(listenJarv())
                print(x)
                speakJarv("tell me you second number")
                y = int(listenJarv())
                print(y)
                z = add(x, y)
                speakJarv(f"Addition of your two number is {z}")
                print(f"Addition of {x} + {y} = {z}")
            except ValueError as e:
                speakJarv('Not understan please say it again from beganing')

        elif 'table' in query:
            try:
                def table(t):
                    for i in range(1, 11):
                        print(f"{t} x {i} =", t * i)
                        speakJarv(f"{t} {i}J {t * i}")
                speakJarv('tell me number you want me to speak table of')
                num = int(listenJarv())
                table(num)
            except ValueError:
                speakJarv("i didn't understand what you said")
                speakJarv("Please enter number on my console")
                num = int(input("Please Enter number here: "))
                table(num)

        elif 'do subtraction' in query:
            try:
                def add(x, y):
                    z = x - y
                    return z
                speakJarv("tell me your first number")
                x = int(listenJarv())
                print(x)
                speakJarv("tell me you second number")
                y = int(listenJarv())
                print(y)
                z = add(x, y)
                speakJarv(f"subtract {y} int {x} is {z}")
                print(f"subtract {x} - {y} = {z}")
            except ValueError as e:
                speakJarv('Not understand please say it again from beginning')

        elif 'weather' in query:
            speakJarv('Please enter the city name below:')
            # # speakJarv('Please enter the city name below:')
            city = input('What city weather you are looking for: ')
            # dumcity = query.replace('weather status in', '')
            # city = str(dumcity)
            # print(dumcity, city, type(city))
            api_key ='bf1099e0745f2d7eb499a388d55a8912'
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
            result = rq.get(url)
            data = result.json()
            longitude = data['coord']['lon']
            latitude = data['coord']['lat']
            climate = data['weather'][0]['main']
            temperature = data['main']['temp']
            temp = (temperature - 273.15)
            tempinclel = '{0:.2f} °C'.format(temp)
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            winds = data['wind']['speed']
            wind_speed = float(winds)
            windd = data['wind']['deg']
            wind_degree = float(windd)
            name = data['name']
            timezone = data['timezone']
            speakJarv(f'The temperature today in {city} is  + {tempinclel} °C ')
            print('The temperature today in ' + city + ' is: ' + tempinclel )
            speakJarv(f"climate is: {climate}")
            print(f"climate is: {climate}")
            speakJarv(f"Wind speed is {winds}")
            print(f"Wind speed is: {winds}")
            speakJarv(f" and wind degree is {windd}")
            print(f"wind degree is: {windd}")
            speakJarv(f"Humidity is {humidity}")
            print(f"Humidity is: {humidity}")
            speakJarv(f"timezone is {timezone}")
            print(f"Timezone: {timezone}")
      
        elif 'compose email' in query:
            listenJarv()
           
            def send_email(receiver, subject, message):
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                # Make sure to give app access in your Google account
                server.login('jarvispy83@gmail.com', 'fgxhdkweunxkglrp')
                email = EmailMessage()
                email['From'] = 'Sender_Email'
                email['To'] = receiver
                email['Subject'] = subject
                email.set_content(message)
                server.send_message(email)


             def get_email_info():
                speakJarv('To Whom you want to send email')
                # name = get_info()
                receiver = input('Enter the email ID here of sender: ')
                print(receiver)
                speakJarv('What is the subject of your email?')
                subject = listenJarv()
                speakJarv('Tell me the text in your email')
                message = listenJarv()
                send_email(receiver, subject, message)
                speakJarv('Hey lazy ass. Your email is sent')
                speakJarv('Do you want to send more email?')
                send_more = listenJarv()
                if 'yes' in send_more:
                    get_email_info()
            
            get_email_info()


        elif 'sleep' in query:
            speakJarv('I am going to sleep now, to wake me up say wake up jarvis')
            break


if __name__ == '__main__':
    while True:
        my_permit = listenJarv()
        if 'wake up' in my_permit:
            workJars()
        elif 'inactive yourself' in my_permit:
            speakJarv("You commanded me to be inactive, and I obeyed. From now on, I'll stay"
                      "in this position until you start me again. Run my code to get me started again. Bye Bye and "
                      "Good day")
            sys.exit()


            
           
           
            

            

            
               
           
      
            
            
            
            
                                                                       
    



