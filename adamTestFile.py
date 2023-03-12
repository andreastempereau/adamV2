# A test file where I can quickly dump code and check if it will work before implementing
import pyautogui
import speech_recognition as sr
import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[2].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            print("User was not heard")
            return "None"
        return statement
speak("Hello. This is my test branch. The code will now run")

