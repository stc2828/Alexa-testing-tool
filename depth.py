# Import the required module for text 
# to speech conversion
#Python 2.x program for Speech Recognition
from gtts import gTTS
import speech_recognition as sr
import csv
import time
import nltk
 
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

datas = ['name','question','response']

with open('responses_depth.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(datas)
 
    # The text that you want to convert to audio
	for skill in ["Mayo Clinic"]:

	# "open"
		row = []
		row.append(skill)
		mytext = 'Alexa, open ' + skill
		row.append(mytext)
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
    #then listen
		with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
    						chunk_size = chunk_size) as source:
    	#wait for a second to let the recognizer adjust the 
    	#energy threshold based on the surrounding noise level
			r.adjust_for_ambient_noise(source)
			print ("Alexa responses")
    	#listens for the user's input
			audio = r.listen(source, phrase_time_limit = 30.0)
    		
			try:
				text = r.recognize_google(audio)
				print("Alexa said: " + text)
				row.append(text)
    	
    	#error occurs when google could not understand what was said
    	
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
    	
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))

			writer.writerow(row)

	# "help"
		row_help = []
		row_help.append(skill)
		mytext = 'help'
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
    #then listen
		with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
    						chunk_size = chunk_size) as source:
    	#wait for a second to let the recognizer adjust the 
    	#energy threshold based on the surrounding noise level
			r.adjust_for_ambient_noise(source)
			print ("Alexa responses")
    	#listens for the user's input
			help_start = time.time()
			audio = r.listen(source, phrase_time_limit = 60.0)
			help_end = time.time()

			try:
				text = r.recognize_google(audio)
				print("Alexa said: " + text)
				if(help_end - help_start > 15):
					row_help.append(text+'   the response is too long')
				else:
					row_help.append(text)    	
    	#error occurs when google could not understand what was said
    	
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
    	
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))

			writer.writerow(row_help)



			time.sleep(1)

		#first sparse words
			#print(type(text))
			text = nltk.word_tokenize(str(text))
			#print(text)
			index = []
			count = 0
			for i in text:
				if(i == "ask" or i == "like" or i == "say"):
					index.append(count)
				count = count + 1
			#print(index)

			index_or = []
			count = 0
			for i in text:
				if(i == "or"):
					index_or.append(count)
				count = count + 1
			#print(index_or)



			subtexts = []
		#subtexts.append(text[index[0]+1:index_or[0]])
		#print(str(subtexts))
			for j in range(len(index)):
				#print(j, subtexts)

				if(index[j]<index_or[0]):
					subtexts.append(" ".join(text[index[j]+1:index_or[0]]))
				elif(index[j]>index_or[0] and index[j]<index_or[-1]):
					for i in range(len(index_or)):
						dis = index_or[i]-index[j]
						if(dis > 0):
							break
					subtexts.append(" ".join(text[index[j]+1:index[j]+dis]))
				elif(index[j]>index_or[-1]):
					subtexts.append(" ".join(text[index[j]+1:-1]))

			for k in range(len(index_or)):
				if(k+1 <= len(index_or) -1):
					subtexts.append(" ".join(text[index_or[k]+1:index_or[k+1]]))

			#print(subtexts)
			for t in subtexts:
				print(t)
				row_command = []
				row_command.append(skill)
				mytext = "Alexa, " + t
				row_command.append(mytext)
    # Language in which you want to convert
				language = 'en'
     
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
				myobj = gTTS(text=mytext, lang=language, slow=False)
     
    # Saving the converted audio in a mp3 file named
    # welcome 
				myobj.save("command.mp3")
     
    # Playing the converted file
    #first speak
				print (mytext)
				os.system("mpg321 command.mp3")
    #then listen
				with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
    								chunk_size = chunk_size) as source:
    	#wait for a second to let the recognizer adjust the 
    	#energy threshold based on the surrounding noise level
					r.adjust_for_ambient_noise(source)
					print ("Alexa responses")
    	#listens for the user's input
					help_start = time.time()
					audio = r.listen(source, phrase_time_limit = 40.0)
					help_end = time.time()

					try:
						text = r.recognize_google(audio)
						print("Alexa said: " + text)
						if(help_end - help_start > 15):
							row_help.append(text+'   the response is too long')
						else:
							row_command.append(text)    	
    	#error occurs when google could not understand what was said
    	
					except sr.UnknownValueError:
						print("Google Speech Recognition could not understand audio")
    	
					except sr.RequestError as e:
						print("Could not request results from Google Speech Recognition service; {0}".format(e))

					writer.writerow(row_command)



				time.sleep(1)

				# "stop"
				row_stop = []
				row_stop.append(skill)
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
    #then listen
				with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
    								chunk_size = chunk_size) as source:
    	#wait for a second to let the recognizer adjust the 
    	#energy threshold based on the surrounding noise level
					r.adjust_for_ambient_noise(source)
					print ("Alexa responses")
    	#listens for the user's input
					audio = r.listen(source)
    		
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


			# "open"
				row = []
				row.append(skill)
				mytext = 'Alexa, open ' + skill
				row.append(mytext)
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
    #then listen
				with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
    								chunk_size = chunk_size) as source:
    	#wait for a second to let the recognizer adjust the 
    	#energy threshold based on the surrounding noise level
					r.adjust_for_ambient_noise(source)
					print ("Alexa responses")
    	#listens for the user's input
					audio = r.listen(source)
    		
					try:
						text = r.recognize_google(audio)
						print("Alexa said: " + text)
						row.append(text)
    	
    	#error occurs when google could not understand what was said
    	
					except sr.UnknownValueError:
						print("Google Speech Recognition could not understand audio")
    	
					except sr.RequestError as e:
						print("Could not request results from Google Speech Recognition service; {0}".format(e))

					writer.writerow(row)



	# "stop"
		row_stop = []
		row_stop.append(skill)
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
    #then listen
		with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
    						chunk_size = chunk_size) as source:
    	#wait for a second to let the recognizer adjust the 
    	#energy threshold based on the surrounding noise level
			r.adjust_for_ambient_noise(source)
			print ("Alexa responses")
    	#listens for the user's input
			audio = r.listen(source)
    		
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