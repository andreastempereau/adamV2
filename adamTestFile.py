# A test file where I can quickly dump code and check if it will work before implementing
import time
import sys

# Default Statement \/ \/
# a.speak("Hello. This is my test branch. The code will now run")

# Test Code Goes Here \/ \/

def reverse(str):
    i = 0
    i = len(str) - 1
    out = ""
    while i>-1:
        out+= str[i]
        i -= 1
print(reverse("TSET"))