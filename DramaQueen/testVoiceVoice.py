import pyttsx
import sys
#sys.path.append('/usr/local/lib/python3.6/dist-packages/')
engine = pyttsx.init()
voices = engine.getProperty('voices')

for voice in voices:
    #print(voice.id)
    engine.setProperty('voice', voices[1].id)
    print(voices[1].id)
    engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
