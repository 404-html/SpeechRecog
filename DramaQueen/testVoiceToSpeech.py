import pyaudio
import speech_recognition as sr
import os

index = pyaudio.PyAudio().get_device_count() - 1
print(index)
r = sr.Recognizer()
while (1 == 1):
    with sr.Microphone() as source:
        audio = r.listen(source)
        try: # Requires internet connection all the time.
            speech = r.recognize_google(audio)
            print("you said "+ speech)
            os.system("python testSpeechToText.py " + speech)
            if speech.lower() == "exit":
                break
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Recog Error; {0}".format(e))

