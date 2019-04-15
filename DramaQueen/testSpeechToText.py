import pyttsx
import sys

engine = pyttsx.init()
ongine = pyttsx.init()
engine = pyttsx.init()
engine.setProperty('rate', 150)
string = "";
for i in range(len(sys.argv) - 1):
    string = string + sys.argv[i + 1] + " "
engine.say(string)
engine.runAndWait()
