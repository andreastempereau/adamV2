#This is Adam's Fusion Helper Mode, Activated through the main class

import speech_recognition as sr
import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[2].id')
fusionLoop = True

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

def fusionMode():
     speak("Welcome to Fusion360 Mode...")
     speak("Let's take a look at the your model")
     while fusionLoop:
          speak("What can I do for you?")
          statement = takeCommand().lower()
          if 'new sketch' in statement or 'draw' in statement or 'drawing' in statement:
               if 'square' in statement or 'rectangle' in statement:
                    speak("I am sketching you a rectangle")
                    #CODE TO SKETCH RECTANGLE
               if 'circle' in statement:
                    speak("I am sketching you a circle")
                    #CODE TO SKETCH CIRCLE
               if 'arc' in statement:
                    speak("I am sketching you an arc")
                    #CODE TO SKETCH ARC
               if 'polygon' in statement:
                    speak("I am sketching you a polygon")
                    #CODE TO SKETCH POLYGON
               if 'slot' in statement:
                    speak("I am sketching you a slot")
                    #CODE TO SKETCH SLOT
               if 'spline' in statement:
                    speak("I am sketching a spline")
                    #CODE TO SKETCH SPLINE
               if 'conic' in statement:
                    speak("I am sketchign the conic curve")
                    #CODE TO SKETCH CONIC CURVE