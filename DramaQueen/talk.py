# from gtts import gTTS
# tts = gTTS('hello')
# tts.save('hello.mp3')
import sys, os
sys.path.append("/usr/local/lib/python3.5/dist-packages")
#os.system('sudo python3 -m pip install espeak')


# import pyttsx
# engine= pyttsx.init()
# engine.setProperty('rate',70)
# voices=engine.getProperty('voices')
# for voice in voices:
#     print "Using voice:", repr(voice)
#     engine.setProperty('voice',voice.id)
#     engine.say("Hello Hello Hello")
# engine.runAndWait()
import pyttsx3;
engine = pyttsx3.init();
engine.say("I will speak this text");
engine.runAndWait() ;