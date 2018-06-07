import pyaudio
import wave
import speech_recognition as sr
 

r = sr.Recognizer()

with sr.WavFile("help.wav") as source:
    	#wait for a second to let the recognizer adjust the 
    	#energy threshold based on the surrounding noise level
	r.adjust_for_ambient_noise(source)
    	#listens for the user's input
	audio = r.record(source)
    		
	try:
		text = r.recognize_google(audio)
		print("Alexa said: " + text)
    	
    	#error occurs when google could not understand what was said
    	
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
    	
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
