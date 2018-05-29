# Import the required module for text 
# to speech conversion
#Python 2.x program for Speech Recognition
from gtts import gTTS
import speech_recognition as sr
 
# This module is imported so that we can 
# play the converted audio
import os

#enter the name of usb microphone that you found
#using lsusb
#the following name is only used as an example
mic_name = "Built-in Microphone"
#Sample rate is how often values are recorded
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data)
#here. 
#it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
#Initialize the recognizer
r = sr.Recognizer()

#generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()

#the following loop aims to set the device ID of the mic that
#we specifically want to use to avoid ambiguity.
for i, microphone_name in enumerate(mic_list):
	print(microphone_name)
	if microphone_name == mic_name:
		device_id = i
 
# The text that you want to convert to audio
for j in ["WebMD"]:
	mytext = 'Alexa, open ' + j
 
# Language in which you want to convert
	language = 'en'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
	myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
	myobj.save("1.mp3")
 
# Playing the converted file
#first speak
	print (mytext)
	os.system("mpg321 1.mp3")
#then listen
	with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
						chunk_size = chunk_size) as source:
	#wait for a second to let the recognizer adjust the 
	#energy threshold based on the surrounding noise level
		r.adjust_for_ambient_noise(source)
		print ("Say Something")
	#listens for the user's input
		audio = r.listen(source)
		
		try:
			text = r.recognize_google(audio)
			print("you said: " + text)
	
	#error occurs when google could not understand what was said
	
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
	
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
