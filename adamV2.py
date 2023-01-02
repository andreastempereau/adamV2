import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import subprocess


print('Booting up...')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning Andreas")
        print("Good Morning Andreas")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Andreas")
        print("Good Afternoon Andreas")
    else:
        speak("Good Evening Andreas")
        print("Good Evening Andreas")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("I can't seem to hear you properly")
            return "None"
        return statement

speak("Booting up... One moment Please,,,")
wishMe()


if __name__=='__main__':

    speak("What can I do for you?")
    while True:
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "nothing" in statement or "leave me alone" in statement or "never mind" in statement:
            speak('Of course sir. Let me know if you need anything else.')
            print('Of course sir. Let me know if you need anything else.')
            break



        if 'wikipedia' in statement:
            speak('Checking the web.')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to wikipedia.")
            print(results)
            speak(results)
        elif 'open fusion' in statement:
            speak("A new project sir?")
            subprocess.Popen('C:\\Users\\Andre\\Desktop\\Fusion360.lnk')

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Opening")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Searching for something in particular?")
            time.sleep(5)
            statement = takeCommand().lower()
            if 'not really' in statement or 'no' in statement:
                speak("Of course... Just browsing then.")
            elif 'yeah can you help me' in statement:
                speak("What can I search for you?")
                statement = takeCommand().lower()
                speak("Let me see what I can find for you.")
                webbrowser.get(chrome_path).open(statement)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'open my classes' in statement:
            webbrowser.open_new_tab("https://classroom.google.com/u/3/h")
            speak("Here are your classes sir")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am a natural language model created to help you.')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Andreas. I am a natural language model created to help you.")
            print("I was built by Andreas. I am a natural language model created to help you.")


        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.get(chrome_path).open(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions. What question do you want to ask now?')
            question=takeCommand()
            app_id="U7T44K-25U4986UWV"
            client = wolframalpha.Client('U7T44K-25U4986UWV')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "no" in statement:
            speak("Sure thing. Goodbye.")
            break
        
        speak("Do you need anything else sir?")

time.sleep(5)





