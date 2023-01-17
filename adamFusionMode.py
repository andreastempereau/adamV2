#This is Adam's Fusion Helper Mode, Activated through the main class

import speech_recognition as sr
import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[2].id')
fusionLoop = True
statement2 = ""
i = 0

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

          if "extrude" in statement or 'pull this sketch out' in statement:
               if "INSERT CODE TO CHECK IF NUMBERS IN STATEMENT" in statement:
                    if "INSERT CODE TO CHECK IF A SPECIFIC SKETCH WAS SAID" in statement:
                         if "INSETR CODE TO CHECK IF UNIT OF MEASUREMENT WAS SAID" in statement:
                              speak("Extruding SPECIFIC SKETCH out SPECIFIC NUMBER SPECIFIC UNITS for you now")
                              #INSERT CODE TO PERFORM THIS ACTION

               else:
                    speak("How far do you want this extruded sir?")
                    statement2 = takeCommand().lower()
                    if "CHECK IF SPECIFIC SKETCH WAS SAID" in statement:
                         speak("Extruding SPECIFIC SKETCH" + statement2)
                    else:
                         speak("Which sketch sir?")
                         statement = takeCommand().lower()
                         