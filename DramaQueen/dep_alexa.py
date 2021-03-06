import time
import os
import speech_recognition as sr
import random
#from textblob import Word

Alexa = []
Human = []

recognizer = sr.Recognizer()

with open('script_clean.txt') as fp:
    for line in fp:
        if('alexa' in line):
            Alexa.append(line.split(' ', 1)[1])
        elif('prof' in line):
            Human.append(line.split(' ', 1)[1])
        else:
            print(line)

"""
    This function checks to see if any of the sentences matches atleast 60% to the given sentence. And then returns that sentence index.
    If no sentence is matched 60% it returns -1.
"""
def checkSpeech(line):
    toRet = -1
    count = 0
    lineArr = line.split(' ')
    #totCount = len(lineArr)
    for s in Human:
        totCount = len(s.split(' '))
        toRet += 1
        for w in lineArr:
            #print("\nw : " + w.lower() + "\t\ts : " + s.lower())
            if(w.lower() in s.lower()):
                count += 1
            if(count/float(totCount) * 100 >= 60):
                return toRet
        count = 0
    return -1


"""
    This function listens for the input. if there is an error it speaks the error. if there is no error it returns the speech
"""
def listen():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("error: could not understand audio")
            #os.system('python testSpeechToText.py "Could you please speak better? Alexa can not understand you!"')
        except sr.RequestError as e:
            print("Recog Error; {0}".format(e))
            #os.system('python testSpeechToText.py "Got an error. Check For error"')
    return ""
"""
def newSentence(line):
    words = line.split()
    output = list()
    for word_str in words:
        word_obj = Word(word_str)
        if len(word_str) > 3 and len(word_obj.synsets) > 0:
            random_synset = random.choice(word_obj.synsets)
            random_lemma = random.choice(random_synset.lemma_names)
            output.append(random_lemma.replace('_', ' '))
        else:
            output.append(word_str)
    return " ".join(output)
"""

"""
    Woman speaks the result
"""
def speak(text):
    os.system('google_speech -l en "' + text + '" -e speed 0.95')

"""
    Robot voice speak result
"""
def robotSpeak(text):
    os.system('python testSpeechToText.py ' + text)

speak(Alexa[0])

while (1 == 1):
    human = listen()
    print("Human ==>> \t" + human)
    if (human == ""):
        speak("Honey, I do not understand!")
        #robotSpeak("She did not understand anything you said!")
    #elif ("exit" in human.lower):
    #    break
    else:
        num = checkSpeech(human)
        if(num < len(Alexa)):
            if(num == -1):
                num = random.randint(0, len(Alexa))
                print("Could not find a clear match. Randomizing")
            print("Alexa ==>> \t" + Alexa[num])
            #sentence = newSentence(Alexa[num])
            #print("\n new sentence = " + sentence)
            #speak(sentence)
            speak(Alexa[num])
        else:
            speak("I, I, I, I am very sorry that we could not work something out")
            robotSpeak("Get Out. I have nothing else to tell you. Just. get. out")
            break


"""
for line in Human:
    os.system('google_speech -l en "' + line + '"')
"""
