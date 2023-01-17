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

my_tools = ['hammer', 'dremel', 'needle nosed pliers', 'wood saw', 
            'metal saw', 'saw', 'electrical tape', 'duct tape', 
            'scotch tape', 'measuring tape', 'glue gun', 'wrench', 
            'screwdriver', 'flamethrower', 'welder', 'welding helmet',
            'facemask', 'glasses', 'resistors', 'stepper motors',
            'transitors', 'diodes', 'voltmeter', 'jumper wires',
            'printer filament', 'boat winch', 'aluminum', 'steel rods',
            'drill bits', 'nails', 'screws', 'dremel bits', 'demagnitizer',
            'magnitizer', 'magnet', 'drill', 'impact drill',]
tools_in_left_drawer = ['metal drill bits', 'nails', 'screws', 'dremel bits',
                        'wood drill bits',
                        'hammer', 'dremel', 'needle nosed pliers', 'wood saw', 
                        'stepper motors','demagnitizer','magnitizer', 'magnet', 
                        'hot glue', 'scale']
tools_in_right_drawer = ['']
tools_in_top_shelf_box = ['']
tools_on_top_shelf = ['']
tools_in_alt_floor_bin = ['']
tools_in_main_floor_bin = ['']
tools_on_wall = ['']

def toolSearch(statement):
    for tool in my_tools:
        if tool in statement:
            speak("Let me look for your " + tool)
