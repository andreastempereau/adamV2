import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import tkinter
import os
import time
import numpy as np
import subprocess
import pywhatkit as kt
import imutils
import pandas_datareader as web
import cv2
import pandas as pd
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import adamKerasStockPredictor
import adamFileSearch
import adamFusionMode
import adamPhrases as AP
import pyautogui
import adamMethod as a
import airQualityChecker
import runFile as r

print('Booting up...')
startUp = False
fileSearchLoop = True
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


def AdamStart():
    a.speak("Booting up... One moment Please,,,")
    a.speak("Bootup complete..")
    print("Bootup Complete")
    while True:
        time.sleep(0.5)
        statement = a.takeCommand().lower()
        if "adam" in statement:
            startUp = True
        if "perform complete shutdown" in statement:
            a.speak("I am performing a cold shutdown now...")
            break
        while startUp:
            if statement==0:
                continue

            if "cancel request" in statement:
                a.speak(AP.acknowledge() + "... I will ignore your request")
                time.sleep(3)

            elif "good bye" in statement or "ok bye" in statement or "stop" in statement or "nothing" in statement or "leave me alone" in statement or "never mind" in statement or "shutdown" in statement:
                a.speak(AP.acknowledge() + '... Let me know if you need anything else.')
                startUp = False
                break
            elif 'open' in statement:
                tries = 0
                while True:
                    if 'fusion' in statement:
                        #OPEN FUSION HERE
                        a.speak(AP.acknowledge() + "Let me get that started for you...")
                        a.run_exe_and_keep_running(r"C:\Users\Andre\AppData\Local\Autodesk\webdeploy\production\3f77c28c02b1b466e9d910ef562e48d42f47cc2b\Fusion360.exe")
                        a.speak("A new project sir?")
                        statement = a.takeCommand().lower()
                        if AP.checkYes(statement):
                            a.speak(AP.acknowledge() + "... Would you like me to help analyze some sketchs?")
                            statement = a.takeCommand().lower()
                            if AP.checkYes(statement):
                                a.speak("Let's get started sir... Would you like me to enter observational 3D model mode?")
                                statement = a.takeCommand().lower()
                                if AP.checkYes(statement):
                                    a.speak(AP.acknowledge() + "... Entering now.")
                                    break
                                    #MOVE TO FUSIONMANIPULATING VERSION
                                else:
                                    a.speak("I will be on standby if you need help with sketches")
                                    break

                            elif AP.checkNo(statement):
                                a.speak(AP.acknowledge() + "... I will be on standby...")
                                time.sleep(4)
                                break
                        else:
                            a.speak("Let me know if you need help with sketches")
                            time.sleep(4)
                            break

                    if 'youtube' in statement:
                        webbrowser.open_new_tab("https://www.youtube.com")
                        a.speak("Opening")
                        a.speak("Searching for a specific video?")
                        statement = a.takeCommand().lower()
                        if AP.checkNo(statement):
                            a.speak(AP.acknowledge() + "... Just browsing then.")
                            statement = 'dfgrfs'
                            break
                        elif AP.checkYes(statement):
                            a.speak("What can I search for you?")
                            statement = a.takeCommand().lower()
                            a.speak("Let me see what I can find for you.")
                            webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + statement.replace(" ", "+"))
                            time.sleep(4)
                            break
                        else:
                            a.speak("Let me see what I can find for you")
                            webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + statement.replace(" ", "+"))
                            time.sleep(4)
                            break

                    if 'gmail' in statement:
                        webbrowser.open_new_tab("https://www.gmail.com")
                        a.speak("Google Mail open now")
                        time.sleep(4)
                        break

                    if 'my classes' in statement or 'google classroom' in statement:
                        webbrowser.open_new_tab("https://classroom.google.com/u/3/h")
                        a.speak("Here are your classes sir")
                        time.sleep(4)
                        break
                    
                    if 'google' in statement:
                        webbrowser.open_new_tab("https://www.google.com")
                        a.speak("Searching for something in particular?")
                        statement = a.takeCommand().lower()
                        if AP.checkNo(statement):
                            a.speak(AP.acknowledge() + "... Just browsing then.")
                            statement = 'dfgrfs'
                            break
                        elif AP.checkYes(statement):
                            a.speak("What can I search for you?")
                            statement = a.takeCommand().lower()
                            a.speak("Let me see what I can find for you.")
                            kt.search(statement)
                            time.sleep(4)
                            break
                        else:
                            a.speak("Let me see what I can find for you")
                            kt.search(statement)
                            time.sleep(4)
                            break

                    if "stack overflow" in statement:
                        webbrowser.open_new_tab("https://stackoverflow.com/")
                        a.speak("Here is stackoverflow")
                        break
                    else:
                        if tries > 0:
                            a.speak("I am sorry I am having trouble finding it. Would you like to try yourself?")
                            statement = a.takeCommand().lower()
                            if AP.checkYes(statement):
                                a.speak(AP.acknowledge())
                                tries = 0
                                break
                            else:
                                a.speak(AP.acknowledge() + "...let us try again...")
                                tries = -1
                                statement = " "
                                continue
                        else:
                            a.speak("What can I open for you?")
                            tries += 1
                            statement = a.takeCommand().lower()
                            continue
            elif "air quality" in statement:
                airQualityChecker.adamAirQuality(statement)
            elif "watch" and "door" in statement:
                a.speak(AP.acknowledge() + "...I will arm the house now")
                time.sleep(1)
                a.speak("Sensor A3 is offline... shall I run diagnostics?")
                statement = a.takeCommand().lower()
                if "that's fine" or "i know" in statement:
                    a.speak("Glad to know it was an intentional disable")
                    statement = "break2005"
            elif 'you there' in statement:
                a.speak("For you sir,,, always")
                statement = a.takeCommand().lower()
            elif 'problem' in statement:
                a.speak("What is wrong sir?")
                statement = a.takeCommand().lower()
                continue
            elif 'screenshot' in statement:
                a.speak(AP.acknowledge() + "... Press any key when you are done viewing")
                a.screenshot()
                time.sleep(4)
            elif 'wikipedia' in statement:
                a.speak('Checking the web.')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                a.speak("According to wikipedia.")
                print(results)
                a.speak(results)
            elif 'take over' in statement and 'game' in statement:
                a.speak(AP.acknowledge() + "... How do you want me to control")
                statement = a.takeCommand().lower()
                if 'forward' in statement:
                    a.speak(AP.acknowledge() + "...I will keep your character on the right path")
                    pyautogui.hold('shift', 'w')
            elif 'check fusion sketch' in statement or 'check sketch' in statement:
                a.speak("Let's get started sir... Would you like me to enter observational 3D model mode?")
                statement = a.takeCommand().lower()
                if AP.checkYes(statement):
                    a.speak(AP.acknowledge() + "... Entering now.")
                    #MOVE TO FUSIONMANIPULATING VERSION
                else:
                    a.speak("I will be on standby if you need help with sketches")

            elif 'file search' in statement or 'find a file' in statement or 'find me a file' in statement:
                a.speak("What does the file end in sir?")
                statement = a.takeCommand().lower().replace(" ", "")
                a.speak("What is the name of the file sir?")
                statement2 = a.takeCommand().lower().replace(" ", "") + statement
                a.speak("I will try to find your file. Please note this may take a few minutes as I am searching your entire drive")
                try:
                    adamFileSearch.fileSearch(statement2, statement)
                    a.speak("I found your file sir... I printed it out in the terminal for you.")
                except Exception as e:
                    a.speak("I cannot seem to find the file... Maybe type it in?")
                    statement = a.takeCommand().lower()
                    if AP.checkYes(statement):
                        a.speak(AP.acknowledge())
                        while fileSearchLoop:
                            a.speak("I have created a line in the terminal for you to put the filename in..")
                            fileName = input('Type in file name here (Without extension): ')
                            fileExtension = fileName + input("Type in the file extension: ")
                            try:
                                adamFileSearch.fileSearch(fileName, fileExtension)
                                fileSearchLoop = False
                                a.speak("Thank you sir... Your file location is printed out in the terminal")
                                statement = a.takeCommand().lower()
                                if 'read' in statement:
                                    if len(adamFileSearch.fileSearch(fileName, fileExtension)) > 50:
                                        a.speak("It is rather long sir... Speaking it may take a very long time... Might I suggest jsut reading it?")
                                        statement = a.takeCommand().lower()
                                        if AP.checkNo(statement) or 'read it to me' in statement:
                                            a.speak(AP.acknowledge() + "... You know best...")
                                            a.speak(adamFileSearch.fileSearch(fileName, fileExtension))
                                        else:
                                            a.speak(AP.acknowledge() + "... It is still in the terminal for you to find")
                                            statement = 'dfgrfs'
                                    else:
                                        a.speak(AP.acknowledge())
                                        a.speak(adamFileSearch.fileSearch(fileName, fileExtension))
                                else:
                                    statement = 'dfgrfs'
                                time.sleep(1)
                            except Exception as e:
                                a.speak("I still cannot seem to find the file. Maybe check the capilization and spelling? Would you like to try again?")
                                statement = a.takeCommand().lower()
                                if AP.checkYes(statement):
                                    fileSearchLoop = True
                                else:
                                    a.speak("Apologies for failing to find it...")
                                    fileSearchLoop = False
                                    statement = 'dfgrfs'

                    else:
                        a.speak(AP.acknowledge() + "... Apologies for failing to find it..")
                        time.sleep(2)
            elif 'stock price' in statement:
                a.speak("Creating a Keras Model... Stand by please...")
                a.speak("It seems the next predicted price should be " + adamKerasStockPredictor.trainingDataFunction())
                print(adamKerasStockPredictor.trainingDataFunction())
                statement = a.takeCommand().lower()
                if 'model' in statement or 'graph' in statement:
                    a.speak(AP.acknowledge())
                    adamKerasStockPredictor.closePricePlot()
                else:
                    statement = 'dfgrfs'
                time.sleep(2)

            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                a.speak(f"the time is {strTime}")

            elif 'who are you' in statement or 'what can you do' in statement:
                a.speak('I am a natural language model created to help you.')

            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                a.speak("I was built by Andreas. I am a natural language model created to help you.")
                print("I was built by Andreas. I am a natural language model created to help you.")


            elif 'search'  in statement:
                statement = statement.replace("search", "")
                kt.search(statement)
                time.sleep(3)

            elif "log off" in statement or "sign out" in statement:
                a.speak(AP.acknowledge() + "... your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            elif "no" in statement:
                a.speak(AP.acknowledge() + "... Goodbye.")
                startUp = False
                break
            elif "break2005" in statement:
                break
            elif "later" in statement or "check back with me" in statement:
                a.speak(AP.acknowledge())
                startUp = False
                break
            elif "thank you" in statement:
                a.speak(AP.acknowledge() + "... I am happy to be of assistance")
                startUp = False
                break
            elif 'adam' in statement:
                a.wishMe()
                a.speak("What can I do for you?")
                statement = a.takeCommand().lower()
                continue

            elif 'dfgrfs' in statement:
                time.sleep(1)
            else:
                a.speak("I apologize.. I cannot seem to match a request...")
                time.sleep(1)
            a.speak("Do you need anything else sir?")
            statement = a.takeCommand().lower()
            if AP.checkYes(statement):
                a.speak(AP.acknowledge() + "...what can I do for you?")
                statement = a.takeCommand().lower()
                continue

time.sleep(2)