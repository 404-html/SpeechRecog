import pyaudio
import speech_recognition as sr

index = pyaudio.PyAudio().get_device_count() - 1
print(index)

r = sr.Recognizer()
for i in range(5):
	with sr.Microphone() as source:
	    audio = r.listen(source)

	    try: # Requires internet connection all the time.
	        print("You said " + r.recognize_google(audio))
	    except LookupError:
	        print("Could not understand audio")

