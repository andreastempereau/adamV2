import speech_recognition as sr
import pyttsx3
import datetime
import os
import time
import subprocess
import imutils
import cv2
import pyautogui

outputString = ""
def findFile(endingNotation):
    for dirpath, dirnames, filenames in os.walk("c:\\"): 
        for filename in filenames: 
            if filename.endswith(endingNotation): 
                outputString +=(os.path.join(dirpath, filename))
    return outputString


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[2].id')


def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def run_exe_and_keep_running(filename):
    process = subprocess.Popen([filename])
    print(f"Started process with PID")
    time.sleep(4)

def screenshot():
    pyautogui.screenshot("straight_to_disk.png")
    image = cv2.imread("straight_to_disk.png")
    cv2.imshow("Screenshot", imutils.resize(image, width=600))
    cv2.waitKey(0)

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
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
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