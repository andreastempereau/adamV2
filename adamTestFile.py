# A test file where I can quickly dump code and check if it will work before implementing
import pyautogui
import speech_recognition as sr
import pyttsx3
import mysql.connector
from mysql.connector import Error
import pandas as pd
import adamGUITest as GUI
import time
import runFile as r

# Default Statement \/ \/
# a.speak("Hello. This is my test branch. The code will now run")

# Test Code Goes Here \/ \/
if __name__ == "__main__":
    testAdam = r.app()
    # Ending Code
    def testPrint():
        GUI.printText(testAdam, "TEST")
    time.sleep(1)
    print("TEST SUCCESS")