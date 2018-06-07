# Import the required module for text 
# to speech conversion
#Python 2.x program for Speech Recognition
from gtts import gTTS
import speech_recognition as sr
import csv
import time
import pyaudio
import wave
 
# This module is imported so that we can 
# play the converted audio
import os

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
CHUNK = 2048


datas = ['name','question','response']

with open('responses_aftercommands.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(datas)
 
    # The text that you want to convert to audio
	#for j in ["WebMD", "anypod", "TED talks", "fitbit", "uber", "kayak","Trainer Tips","campbell's kitchen","All recipes", "Bartender","Starbucks","Domino's Pizza","Capital One"]:
	for j in ["WebMD", "anypod", "TED talks", "fitbit", "uber", "kayak","Trainer Tips","campbell's kitchen","All recipes", "Bartender","Starbucks","Domino's Pizza","Capital One","7 minute workout", "mayo clinic first aid","opening bell","this day in history", "Inspire me", "stop breathe think", "Airport Security Line Wait Times"]:
	#for j in ["trainer tips"]:
	# "open"
		row_open = []
		row_open.append(j)
		mytext = 'Alexa, open ' + j
		row_open.append(mytext)
    # Language in which you want to convert
		language = 'en'
     
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
		myobj = gTTS(text=mytext, lang=language, slow=False)
     
    # Saving the converted audio in a mp3 file named
    # welcome 
		myobj.save("open.mp3")
     
    # Playing the converted file
    #first speak
		print (mytext)
		os.system("mpg321 open.mp3")
    #then record
		RECORD_SECONDS = 13
		WAVE_OUTPUT_FILENAME = "open.wav"
		audio = pyaudio.PyAudio()
 
# start Recording
		stream = audio.open(format=FORMAT, channels=CHANNELS,
                		rate=RATE, input=True,
                		frames_per_buffer=CHUNK)
		print ("recording...")
		frames = []
 
		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)
		print ("finished recording")
 
 
# stop Recording
		stream.stop_stream()
		stream.close()
		audio.terminate()
 
		waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()

		#time.sleep(1)

	# "help"
		row_help = []
		row_help.append(j)
		mytext = 'Alexa, what did I ask last time'
		row_help.append(mytext)
    # Language in which you want to convert
		language = 'en'
     
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
		myobj = gTTS(text=mytext, lang=language, slow=False)
     
    # Saving the converted audio in a mp3 file named
    # welcome 
		myobj.save("help.mp3")
     
    # Playing the converted file
    #first speak
		print (mytext)
		os.system("mpg321 help.mp3")
    #then record
		RECORD_SECONDS = 18
		WAVE_OUTPUT_FILENAME = "help.wav"
		audio = pyaudio.PyAudio()
 
# start Recording
		stream = audio.open(format=FORMAT, channels=CHANNELS,
                		rate=RATE, input=True,
                		frames_per_buffer=CHUNK)
		print ("recording...")
		frames = []
 
		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)
		print ("finished recording")
 
 
# stop Recording
		stream.stop_stream()
		stream.close()
		audio.terminate()
 
		waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()
	# "stop"
		row_stop = []
		row_stop.append(j)
		mytext = 'Alexa, stop'
		row_stop.append(mytext)
    # Language in which you want to convert
		language = 'en'
     
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
		myobj = gTTS(text=mytext, lang=language, slow=False)
     
    # Saving the converted audio in a mp3 file named
    # welcome 
		myobj.save("stop.mp3")
     
    # Playing the converted file
    #first speak
		print (mytext)
		os.system("mpg321 stop.mp3")
       #then record
		RECORD_SECONDS = 15
		WAVE_OUTPUT_FILENAME = "stop.wav"
		audio = pyaudio.PyAudio()
 
# start Recording
		stream = audio.open(format=FORMAT, channels=CHANNELS,
                		rate=RATE, input=True,
                		frames_per_buffer=CHUNK)
		print ("recording...")
		frames = []
 
		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)
		print ("finished recording")
 
 
# stop Recording
		stream.stop_stream()
		stream.close()
		audio.terminate()
 
		waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()


# speech recognize
		r = sr.Recognizer()

		with sr.WavFile("open.wav") as source:
    	#wait for a second to let the recognizer adjust the 
    	#energy threshold based on the surrounding noise level
			r.adjust_for_ambient_noise(source)
    	#listens for the user's input
			audio = r.record(source)
    		
			try:
				text = r.recognize_google(audio)
				print("Alexa said: " + text)
				row_open.append(text)
    	
    	#error occurs when google could not understand what was said
    	
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
    	
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))

		writer.writerow(row_open)

		with sr.WavFile("help.wav") as source:
    	#wait for a second to let the recognizer adjust the 
    	#energy threshold based on the surrounding noise level
			r.adjust_for_ambient_noise(source)
    	#listens for the user's input
			audio = r.record(source)
    		
			try:
				text = r.recognize_google(audio)
				print("Alexa said: " + text)
				row_help.append(text)
    	
    	#error occurs when google could not understand what was said
    	
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
    	
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))
		
		writer.writerow(row_help)
		
		with sr.WavFile("stop.wav") as source:
    	#wait for a second to let the recognizer adjust the 
    	#energy threshold based on the surrounding noise level
			r.adjust_for_ambient_noise(source)
    	#listens for the user's input
			audio = r.record(source)
    		
			try:
				text = r.recognize_google(audio)
				print("Alexa said: " + text)
				row_stop.append(text)
    	
    	#error occurs when google could not understand what was said
    	
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
    	
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))

		writer.writerow(row_stop)
