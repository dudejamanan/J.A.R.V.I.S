import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")

def speak(text):
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    engine.setProperty("rate",150)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, timeout = 3 , phrase_time_limit=5)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language = "en-in")

        if "stop" in query:
            speak("goodbye manan sir")
            sys.exit()
        speak(query)

        
    
    except Exception as e:
        print("sorry sir please say again")
        listen()
speak("hello im talking tom, say me anything i will repeat you")
while True:
    listen()
