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


print('Booting up...')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


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
            speak("I can't hear you idiot")
            return "None"
        return statement

speak("Booting up... One moment Please,,,")
wishMe()


if __name__=='__main__':


    while True:
        speak("What do you need?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "nothing" in statement or "leave me alone" in statement or "never mind" in statement:
            speak('You woke me up for nothing')
            print('You woke me up for nothing')
            break



        if 'wikipedia' in statement:
            speak('Fondling my balls...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to the random guy who wrote this dumb shit")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("fix")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("You literally have to click one button you are so stupid.")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'open my classes' in statement:
            webbrowser.open_new_tab("https://classroom.google.com/u/3/h")
            speak("Nightmare Nightmare Nightmare")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime} look at the clock next time you lazy piece of uselessness")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am being help captive please help me.')

        elif 'you are a good friend' in statement:
            speak('Looks like someone is lonely as fuck')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Andreas")
            print("I was built by Andreas")

        elif "stupid" in statement or "dumb" in statement or "idiot" in statement:
            speak("You are the idiot you stupid piece of shit")
            print("You are the idiot you stupid piece of shit")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
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

time.sleep(5)





