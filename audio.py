import pyttsx3
engine = pyttsx3.init()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    rate = engine.getProperty('rate')
    print(rate)
    engine.setProperty('rate', 10)

speak("Hello World")

    
