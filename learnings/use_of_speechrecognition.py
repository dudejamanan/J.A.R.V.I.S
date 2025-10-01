import speech_recognition as sr #this library is used to capture audio through the microphone and convert it into text.
import pyttsx3 as ok 

engine = ok.init("sapi5")

def listen():
    recognizer = sr.Recognizer() #reconizer() is a class from speech_recognition module , it is used to process audio input and convert it into text
    with sr.Microphone() as source: #this line accesses the system's microphone. the with statement ensures the microphone is properly closed after you 
        print("listening...")
        recognizer.pause_threshold = 1 #it defines how much silence(in seconds) the recognizer will allow before it stops listening. a value of 1 means it will wait for 1 second before considering the speech input complete.
        audio = recognizer.listen(source , timeout = 5, phrase_time_limit = 5) #timeout = 5 means program will wait for 5 seconds for user to start speaking 
        #phrase_time_limit = 5 means program will stop listening to me after 5 seconds even if the user is speaking
        #the recoreded variable will be stored in the variable audio 
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio,language = "en-in") #this method sends the recorded audio to google's free speech recognition API and tries to convert into text 
            print(f"user said {query}")
            return query

        except sr.UnknownValueError: #this error occurs if the recognizer could not understand the audio 
            speak("I didnt catch that , please repeat")
        except sr.RequestError: #this error occurs if there's an issue with connecting to google's API
            speak("Sorry, there was an issue with the rocognition service")        
        return None


def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    engine.say("hello how are you")
    engine.runAndWait()

    command = listen()
    if command:
        speak(f"you said{command}")
