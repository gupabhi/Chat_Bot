#https://api.wolframalpha.com/v1/spoken?i=father+of+son+of+dharmendra&appid=HQWY5J-34GREV68GE

import urllib
import speech_recognition as sr
import pyttsx as pt
from nltk import word_tokenize,Text,pos_tag

engine = pt.init()
engine.setProperty('rate', 190)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
	print("I'm ready now\n")
	audio = r.listen(source)

# def Speech_Text ():
# 	txt="null"
# 	# recognize speech using Google Speech Recognition
# 	try:
# 	    # for testing purposes, we're just using the default API key
# 	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
# 	    # instead of `r.recognize_google(audio)`
# 	    txt = r.recognize_google(audio)
# 	    print("Speech Recognition thinks you said :\n" + txt)
# 	except sr.UnknownValueError:
# 	    print("Speech Recognition could not understand audio")
# 	except sr.RequestError as e:
# 	    print("Please make sure you are connected to the internet; {0}".format(e))
# 	return txt


def construct_url (before, between, after):
	return (before+between+after)

def get_answer (query):
	fquery = query.replace(" ","+")
	url = construct_url ("https://api.wolframalpha.com/v1/spoken?i=",fquery,"&appid=HQWY5J-34GREV68GE")
	response = urllib.urlopen(url)
	return (response.read())

def nlp (sentence):

	tokens = word_tokenize(sentence)
	tag = pos_tag(tokens)
	return tag

# def check_command (tag):
	
# 	for word in tag:
# 		if word[0]=='right':
# 			return 'r'
# 		elif  word[0]=='left':
# 			return 'l'
# 		elif word[0]=='forward':
# 			return 'f'
# 		elif word[0]=='backward':
# 			return 'b'
	
# 	return 'n'	
		
#txt = Speech_Text ()
# for i in range(10):

txt = raw_input("AChat: ")
out = check_command( nlp(txt))

if out == 'n':
	ans = get_answer(txt)
	print (ans)
	engine.say(ans+'!')
	engine.runAndWait()

else:
	print out


		
