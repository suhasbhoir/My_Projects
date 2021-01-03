import time as ti
import datetime as dt
import pyttsx3 as py3
import speech_recognition as sr 
import PyAudio

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
class Jarvis:
    def speakJar(inp):
        engine = py3.init()
        voices = engine.getProperty('voices') 
        volume = engine.getProperty('volume')
        engine.setProperty('rate', 125)
        engine.setProperty('volume',1.0)
        engine.setProperty('voice', voices[0].id)
        engine.say(inp)
        engine.runAndWait()

    def timeJar():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            print("Good Monrning")
        elif hour >= 12 and hour <= 15:
            print("Good afternoon")
        elif hour >= 15 and hour <= 21:
            print("Good evening")
        else:
            print("Good Night")

    def micJar():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Please Say Something, I am Listning...')
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print('Jarvis Thinks you said' + r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print('Jarvis could not recognize the audio')
        except sr.RequestError as e:
            print(f'sphinx errors; {e}')

    micJar()
    



