# A test file where I can quickly dump code and check if it will work before implementing
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
outputString = ""
fullFileName = "adamTestFile.py"
fileIndexInt = 0
fileOutputPath = ""
fileExtension = ".py"
fileSearchBoolean = True
fileCheckerBackIndex = 0
fileCheckerFrontIndex = 0

for dirpath, dirnames, filenames in os.walk("c:\\"): 
     for filename in filenames: 
          if filename.endswith(".py"): 
               outputString +=(os.path.join(dirpath, filename))
fileIndexInt = outputString.find(fullFileName)
fileCheckerBackIndex = fileIndexInt-1
fileCheckerFrontIndex = fileIndexInt
while fileSearchBoolean:
     if outputString[fileCheckerBackIndex:fileCheckerFrontIndex] != ":":
          fileOutputPath = outputString[fileCheckerBackIndex:fileIndexInt + len(fullFileName)]
          fileCheckerBackIndex -= 1
          fileCheckerFrontIndex -=1
     if outputString[fileCheckerBackIndex:fileIndexInt] == ":":
          fileSearchBoolean = False
          fileOutputPath = outputString[fileCheckerBackIndex-1:fileIndexInt + len(fullFileName)]
print(fileOutputPath)