# A test file where I can quickly dump code and check if it will work before implementing
import time
import sys

# Default Statement \/ \/
# a.speak("Hello. This is my test branch. The code will now run")

# Test Code Goes Here \/ \/

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

print_slow("Type whatever you want here")