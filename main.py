import speech_recognition as sr
import webbrowser
import pyttsx3
from pocketsphinx import LiveSpeech
import musicLibrary
import requests
from gtts import gTTS
import pygame
import time
import os

rcogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your own api key"

def speak_old(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    rate = engine.getProperty('rate')
    print(rate)
    engine.setProperty('rate', 120)


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

# Initialize Pygame
    pygame.init()

# Initialize the mixer module
    pygame.mixer.init()

# Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

# Play the MP3 file
    pygame.mixer.music.play()

# Keep the program running long enough to hear the sound
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def processcommand(c):
    if "open google" in c.lower():
        speak("khul jaa sim sim")
        webbrowser.open("https://google.com")
    
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    
    elif "open linkdin" in c.lower():
        speak("opening lindin")
        webbrowser.open("https://linkdln.in")
    
    elif "open hamster" in c.lower():
        speak("sharam kar le")
        webbrowser.open("https://x.com/BhauMeme/status/1154057212370624514/photo/1")
    
    elif "open calculator" in c.lower():
        speak("opening calculator")
        webbrowser.open("C:\Windows\System32\calc.exe")
    
    elif"open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    
    elif"open spotify" in c.lower():
        speak("opening spotify")
        webbrowser.open("https://open.spotify.com/")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        speak("playing your song")
        webbrowser.open(link)

    elif "news" in c.lower():
        speak("ok")
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=your own api key")
        

        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

        # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        #let openai habdle the request
        pass

if __name__ == "__main__":
    speak("hi dear")

    while True:

        r = sr.Recognizer()
        print("recognizing....")

        # recognize speech using Sphinx
        try:
            
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            
            #work if only tell jarvis
            word = r.recognize_google(audio)
            if(word.lower() == "hello jenny"):
                speak("how may i help you....")
                 
                #listen for command

                with sr.Microphone() as source:
                    print("Jenny is listening you")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

    

