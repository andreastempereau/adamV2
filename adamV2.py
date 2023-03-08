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
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import adamKerasStockPredictor
import adamFileSearch
import adamFusionMode
import pyautogui

print('Booting up...')
startUp = False
fileSearchLoop = True
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[2].id')
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

outputString = ""
def findFile(endingNotation):
    for dirpath, dirnames, filenames in os.walk("c:\\"): 
        for filename in filenames: 
            if filename.endswith(endingNotation): 
                outputString +=(os.path.join(dirpath, filename))
    return outputString

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
def callback(recognizer, audio):
    print(recognizer.recognize_google(audio))

def backgroundListen(methodToRun):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
    stop_listening = recognizer.listen_in_background(mic, callback)
    methodToRun()
    stop_listening()


speak("Booting up... One moment Please,,,")
speak("Bootup complete..")
print("Bootup Complete")

if __name__=='__main__':
    while True:
        time.sleep(0.5)
        statement = takeCommand().lower()
        if "adam" in statement:
            startUp = True
        if "perform complete shutdown" in statement:
            speak("I am performing a cold shutdown now...")
            break
        while startUp:
            if statement==0:
                continue

            if "cancel request" in statement:
                speak("Of course sir... I will ignore your request")
                time.sleep(3)

            elif "good bye" in statement or "ok bye" in statement or "stop" in statement or "nothing" in statement or "leave me alone" in statement or "never mind" in statement or "shutdown" in statement:
                speak('Of course sir. Let me know if you need anything else.')
                startUp = False
                break
            elif "watch" and "door" in statement:
                speak("I will arm the house now...")
                time.sleep(1)
                speak("Sensor A3 is offline... shall I run diagnostics?")
                statement = takeCommand().lower()
                if "that's fine" or "i know" in statement:
                    speak("Glad to know it was an intentional disable")
                    statement = "break2005"
            elif 'you there' in statement:
                speak("For you sir,,, always")
                statement = takeCommand().lower()
            elif 'problem' in statement:
                speak("What is wrong sir?")
                statement = takeCommand().lower()
                continue
            elif 'wikipedia' in statement:
                speak('Checking the web.')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to wikipedia.")
                print(results)
                speak(results)
            elif 'take over' in statement and 'game' in statement:
                speak("Sure thing. How do you want me to control")
                statement = takeCommand().lower()
                if 'forward' in statement:
                    speak("Of course I will keep your character on the right path")
                    pyautogui.hold('shift', 'w')
            elif 'check fusion sketch' in statement or 'check sketch' in statement:
                speak("Let's get started sir... Would you like me to enter observational 3D model mode?")
                statement = takeCommand().lower()
                if 'sure' in statement or 'yes' in statement:
                    speak("Of course sir. Entering now.")
                    #MOVE TO FUSIONMANIPULATING VERSION
                else:
                    speak("I will be on standby if you need help with sketches")
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
                        else:
                            speak("I will be on standby if you need help with sketches")

                    elif 'no' in statement or 'not' in statement:
                        speak("Sure thing sir... I will be on standby...")
                        time.sleep(4)
                else:
                    speak("Let me know if you need help with sketches")
                    time.sleep(4)

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("Opening")
                speak("Searching for a specific video?")
                statement = takeCommand().lower()
                if 'not really' in statement or 'no' in statement:
                    speak("Of course... Just browsing then.")
                    statement = 'dfgrfs'
                elif 'yeah' in statement or 'yes' in statement:
                    speak("What can I search for you?")
                    statement = takeCommand().lower()
                    speak("Let me see what I can find for you.")
                    kt.search(statement)
                    time.sleep(4)
                else:
                    speak("Let me see what I can find for you")
                    webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + statement.replace(" ", "+"))
                    time.sleep(4)
                
            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Searching for something in particular?")
                statement = takeCommand().lower()
                if 'not really' in statement or 'no' in statement:
                    speak("Of course... Just browsing then.")
                    statement = 'dfgrfs'
                elif 'yeah' in statement or 'yes' in statement:
                    speak("What can I search for you?")
                    statement = takeCommand().lower()
                    speak("Let me see what I can find for you.")
                    kt.search(statement)
                    time.sleep(4)
                else:
                    speak("Let me see what I can find for you")
                    kt.search(statement)
                    time.sleep(4)
            elif 'file search' in statement or 'find a file' in statement or 'find me a file' in statement:
                speak("What does the file end in sir?")
                statement = takeCommand().lower().replace(" ", "")
                speak("What is the name of the file sir?")
                statement2 = takeCommand().lower().replace(" ", "") + statement
                speak("I will try to find your file. Please note this may take a few minutes as I am searching your entire drive")
                try:
                    adamFileSearch.fileSearch(statement2, statement)
                    speak("I found your file sir... I printed it out in the terminal for you.")
                except Exception as e:
                    speak("I cannot seem to find the file... Maybe type it in?")
                    statement = takeCommand().lower()
                    if 'sure' in statement or 'yes' in statement or 'yeah' in statement or 'ok' in statement:
                        speak('Of course sir.. ')
                        while fileSearchLoop:
                            speak("I have created a line in the terminal for you to put the filename in..")
                            fileName = input('Type in file name here (Without extension): ')
                            fileExtension = fileName + input("Type in the file extension: ")
                            try:
                                adamFileSearch.fileSearch(fileName, fileExtension)
                                fileSearchLoop = False
                                speak("Thank you sir... Your file location is printed out in the terminal")
                                statement = takeCommand().lower()
                                if 'read' in statement:
                                    if len(adamFileSearch.fileSearch(fileName, fileExtension)) > 50:
                                        speak("It is rather long sir... Speaking it may take a very long time... Might I suggest jsut reading it?")
                                        statement = takeCommand().lower()
                                        if 'no' in statement or 'nah' in statement or 'read it to me' in statement:
                                            speak("Sure thing sir.. You know best...")
                                            speak(adamFileSearch.fileSearch(fileName, fileExtension))
                                        else:
                                            speak("Splendid... It is still in the terminal for you to find")
                                            statement = 'dfgrfs'
                                    else:
                                        speak("Of course sir..")
                                        speak(adamFileSearch.fileSearch(fileName, fileExtension))
                                else:
                                    statement = 'dfgrfs'
                                time.sleep(1)
                            except Exception as e:
                                speak("I still cannot seem to find the file. Maybe check the capilization and spelling? Would you like to try again?")
                                statement = takeCommand().lower()
                                if 'yes' in statement or 'sure' in statement or 'ok' in statement or 'yeah' in statement:
                                    fileSearchLoop = True
                                else:
                                    speak("Apologies for failing to find it...")
                                    fileSearchLoop = False
                                    statement = 'dfgrfs'

                    else:
                        speak("Of course sir... Apologies for failing to find it..")
                        time.sleep(2)
            elif 'stock price' in statement:
                speak("Creating a Keras Model... Stand by please...")
                speak("It seems the next predicted price should be " + adamKerasStockPredictor.trainingDataFunction())
                print(adamKerasStockPredictor.trainingDataFunction())
                statement = takeCommand().lower()
                if 'model' in statement or 'graph' in statement:
                    speak("Of course sir...")
                    adamKerasStockPredictor.closePricePlot()
                else:
                    statement = 'dfgrfs'
                time.sleep(2)
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
                webbrowser.open_new_tab("https://stackoverflow.com/")
                speak("Here is stackoverflow")

            elif 'search'  in statement:
                statement = statement.replace("search", "")
                kt.search(statement)
                time.sleep(3)

            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            elif "no" in statement:
                speak("Sure thing. Goodbye.")
                startUp = False
                break
            elif "break2005" in statement:
                break
            elif "later" in statement or "check back with me" in statement:
                speak("Of course sir...")
                startUp = False
                break
            elif "thank you" in statement:
                speak("Of course sir... I am happy to be of assistance")
                startUp = False
                break
            elif 'adam' in statement:
                wishMe()
                speak("What can I do for you?")
                statement = takeCommand().lower()
                continue
            elif 'dfgrfs' in statement:
                time.sleep(1)
            else:
                speak("I apologize.. I cannot seem to match a request...")
                time.sleep(1)
            speak("Do you need anything else sir?")
            statement = takeCommand().lower()

time.sleep(2)