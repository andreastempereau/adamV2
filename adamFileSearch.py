import os
def fileSearch(fileName, extension):
     outputString = ""
     fullFileName = fileName
     fileIndexInt = 0
     fileOutputPath = ""
     fileExtension = extension
     fileSearchBoolean = True
     fileCheckerBackIndex = 0
     fileCheckerFrontIndex = 0
     for dirpath, dirnames, filenames in os.walk("c:\\"): 
          for filename in filenames: 
               if filename.endswith(fileExtension): 
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