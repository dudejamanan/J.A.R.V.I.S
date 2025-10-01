# pyttsx3 is a python lirary for text to speech conversion 
import pyttsx3

#initialize the speech engine 
engine = pyttsx3.init("sapi5") #sapi5 = microsoft speech api version 5

#set properties
engine.setProperty("rate",150) #speed of speech 
engine.setProperty("volume",0.9) #volume can be set from 0 to 1

#get available voices and set a voice 
voices = engine.getProperty("voices") #gets a list of available voices on your system. Each voice in this list has properties such as its ID, name, gender, and language.
engine.setProperty("voice",voices[0].id) #voice[0].id for male and voice[1].id for female 

#convert text to speech
engine.say("hello i am manan dudeja's jarvis lesssgoooooooo")
engine.runAndWait()