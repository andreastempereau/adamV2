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
import pywhatkit as kt

print('Booting up...')
startUp = False
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def run_exe_and_keep_running(filename):
    process = subprocess.Popen([filename])
    print(f"Started process with PID")
    time.sleep(4)

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
            print("User was not heard")
            return "None"
        return statement

speak("Booting up... One moment Please,,,")
speak("Bootup complete..")

if __name__=='__main__':
    while True:
        time.sleep(0.5)
        statement = takeCommand().lower()
        if "adam" in statement:
            startUp = True
            wishMe()
            speak("What can I do for you?")
        if "perform cold shutdown" in statement:
            speak("I am performing a cold shutdown now...")
            break
        while startUp:
            statement = takeCommand().lower()
            if statement==0:
                continue

            if "cancel request" in statement:
                speak("Of course sir... I will ignore your request")
                time.sleep(3);

            elif "good bye" in statement or "ok bye" in statement or "stop" in statement or "nothing" in statement or "leave me alone" in statement or "never mind" in statement or "shutdown" in statement:
                speak('Of course sir. Let me know if you need anything else.')
                startUp = False
                break

            elif 'wikipedia' in statement:
                speak('Checking the web.')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to wikipedia.")
                print(results)
                speak(results)
            elif 'open fusion' in statement:
                #OPEN FUSION HERE
                speak("Let me get that started for you...")
                run_exe_and_keep_running(r"C:\Users\Andre\AppData\Local\Autodesk\webdeploy\production\3f77c28c02b1b466e9d910ef562e48d42f47cc2b\Fusion360.exe")
                speak("A new project sir?")
                statement = takeCommand().lower()
                if 'yes' in statement or 'basically' in statement or 'yeah' in statement:
                    speak("Of course... Would you like me to help analyze some sketchs?")
                    statement = takeCommand().lower()
                    if 'sure' in statement or 'yes' in statement:
                        speak("Let's get started sir... Would you like me to enter observational 3D model mode?")
                        statement = takeCommand().lower()
                        if 'sure' in statement or 'yes' in statement:
                            speak("Of course sir. Entering now.")
                            #MOVE TO FUSIONMANIPULATING VERSION
                    elif 'no' in statement or 'not' in statement:
                        speak("Sure thing sir... I will be on standby...")
                        time.sleep(4)
                else:
                    speak("Let me know if you need help with sketches")
                    time.sleep(4)

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("Opening")
                time.sleep(4)

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Searching for something in particular?")
                statement = takeCommand().lower()
                if 'not really' in statement or 'no' in statement:
                    speak("Of course... Just browsing then.")
                elif 'yeah' in statement or 'yes' in statement:
                    speak("What can I search for you?")
                    statement = takeCommand().lower()
                    speak("Let me see what I can find for you.")
                    kt.search(statement)
                    time.sleep(4)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("https://www.gmail.com")
                speak("Google Mail open now")
                time.sleep(4)

            elif 'open my classes' in statement:
                webbrowser.open_new_tab("https://classroom.google.com/u/3/h")
                speak("Here are your classes sir")
                time.sleep(4)

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
                time.sleep(4)

            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            elif "no" in statement:
                speak("Sure thing. Goodbye.")
                startUp = False
                break
            elif "later" in statement or "check back with me" in statement:
                speak("Of course sir...")
                startUp = False
                break
            else:
                speak("I apologize.. I cannot seem to match a request...")
                time.sleep(1)

            speak("Do you need anything else sir?")

time.sleep(4)





