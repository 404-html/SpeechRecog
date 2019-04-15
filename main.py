#!/usr/bin/python
from flask import render_template, abort, jsonify, Flask, request, url_for, json, redirect, Response, session, g
import random
from convo import dic 

app = Flask(__name__)

Alexa = []
Human = []


@app.route("/")
def hello():
	return render_template('index.html')

@app.route('/getSpeech', methods=["GET", 'POST'])
def getSpeech():
	if request.method == 'POST':
		human = request.json['speech'].encode("utf-8").lower()
		print("Professor: " , human)
		count = 1

		filtering  = {}
		unique = {}
		human = toLetter(human)
		human = human.split()
		import re
		for key, value in dic.items():
			realKey = key
			key = key.lower()
			key = toLetter(key)
			key = re.sub(' +' , ' ', key)
			key = key.split()
			for word in human: 
				for k in key:
					if word == k:
						if realKey not in filtering and word not in unique:
							filtering[realKey] = 1
							unique[word] = word
						elif realKey in filtering and word not in unique:
							filtering[realKey] +=1 
							unique[word] = word
			unique={}

		ret = []
		for key, value in filtering.items():
			ret.append({key: value, 'value': value, 'reply': dic[key]})

		ret.sort(key=lambda x: x['value'], reverse=True)
		

		# for item in ret:
		# 	print(item['reply'] )


		response = None
		for item in ret:
			response = item['reply']
			break
		
		if response == None:
			response = ""
			response += getSpeech()

		
		return jsonify({'alexa':response})




def toLetter(string):
	temp = ''
	for ch in string:
		if ch.isalpha() or ch == ' ' or ch.isdigit(): 
			temp+=ch

	return temp



Alexa = []
Human = []

def checkSpeech(line):
	toRet = -1
	count = 0
	lineArr = line.split(' ')
	#totCount = len(lineArr)
	for s in Human:
		totCount = len(s.split(' '))
		toRet += 1
		for w in lineArr:
			if(w.lower() in s.lower()):
				count += 1
			if(count/float(totCount) * 100 >= 60):
				return toRet
		count = 0
	return -1


def getSpeech():
	human = request.json['speech']
	print(human)
	tag_alexa = 'alexa'
	tag_human = "prof"
	with open('clean_script.txt') as fp:
		for line in fp:
			if(tag_alexa in line):
				Alexa.append(line.split(' ', 1)[1])
			elif(tag_human in line):
				Human.append(line.split(' ', 1)[1])

	if len(human) == 0:
		return jsonify({'alexa':'Honey, I do not understand'})
	else:
		num = checkSpeech(human)
		if(num < len(Alexa)):
			if(num == -1):
				num = random.randint(0, len(Alexa))
			return str(Alexa[num])
		else:
			return '"I, I, I, I am very sorry that we could not work something out"'		


if __name__ == "__main__":
    app.run(debug=True)
