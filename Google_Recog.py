# This script will take audio, from extract noun

import speech_recognition as sr
import Find_Keys

# This is speak response 
import pyttsx
response = 'Taylor Swift'
engine = pyttsx.init()
engine.setProperty('rate', 135)
#engine.say(response)
engine.runAndWait()

# Record Audio
def audio_str ():
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Ask Query!!")
	    audio = r.listen(source)
	 	
	# Speech recognition using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    print("You said: " + r.recognize_google(audio))
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))

	return str(r.recognize_google(audio))	


print Find_Keys.Give_Noun (audio_str())