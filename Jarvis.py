import datetime as dt
import pyttsx3 as py3
import speech_recognition as sr 
import wikipedia as wiki
import webbrowser as wb
import os 
import subprocess as sp

# class Jarvis:
def speakJarv(inp):
    engine = py3.init()
    voices = engine.getProperty('voices') 
    volume = engine.getProperty('volume')
    engine.setProperty('rate', 120)
    engine.setProperty('volume',1.0)
    engine.setProperty('voice', voices[0].id)
    engine.say(inp)
    engine.runAndWait()

def wishJarv():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speakJarv("Good Monrning")
        speakJarv("myself Jarvis. How may i help you")
    elif hour >= 12 and hour <= 15:
        speakJarv("Good afternoon")
        speakJarv("myself Jarvis. How may i help you")
    elif hour >= 15 and hour <= 21:
        speakJarv("Good evening")
        speakJarv("myself Jarvis. How may i help you")
    else:
        speakJarv("Good Night")
        speakJarv("myself Jarvis. How may i help you")

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
    wishJarv()
    while True:
        query = listenJarv()

        if 'how are you doing' in query:
            speakJarv("I am good")

        elif 'who are you' in query:
            speakJarv("i am a fictional artificial intelligence that first appeared in the Marvel Cinematic Universe where he was voiced by Paul Bettany in Iron Man1 and Iron Man 2")

        elif 'open youtube' in query:
            wb.open("youtube.com")

        elif 'open wikipedia' in query:
            wb.open("en.wikipedia.org")

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
            os.system("taskkill /f /im pycharm64.exe")
            speakJarv("Closing pychaarm")

        elif 'open pycharm' in query:
            opencharm = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe'
            os.startfile(opencharm)

        elif 'close pycharm' in query:
            os.system("taskkill /f /im pycharm64.exe")
            speakJarv("Closing pycharm")
        
        elif 'open git bash' in query:
            opengit = 'C:\\Program Files\\Git\\git-bash.exe'
            os.startfile(opengit)
            
        elif 'close git bash' in query:
            os.system("taskkill /f /im mintty.exe")
            speakJarv("Closing git bash")  

        elif 'open outlook' in query:
            opengit = "C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"
            os.startfile(opengit)
            
        elif 'close outlook' in query:
            os.system("taskkill /f /im OUTLOOK.EXE")
            speakJarv("Closing git bash")  
           
         
            
            
            
                                                                       
    



