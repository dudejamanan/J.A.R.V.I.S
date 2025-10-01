import datetime
import pyttsx3
import speech_recognition as sr
import sys
import cv2

engine = pyttsx3.init()
def speak(text):
    engine.setProperty("rate",150)
    engine.setProperty("volume",0.9)

    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    print(text)
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour) #this prints hour of abhi ka time in int
    if hour>=0 and hour<=12:
        speak("good morning kalai priya maam. i am solar jarvis")
    elif hour>12 and hour<16:
        speak("good afternoon kalai priya maam. i am solar jarvis")
    else:
        speak("good evening kalai priya maam. i am solar jarvis")
    

def listen():
    r= sr.Recognizer() 
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1 
        audio = r.listen(source,timeout = 5, phrase_time_limit = 10) 
        
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = "en-in")
        print(f"user said: {query}")
        speak(query)
    except Exception as e:
        speak ("say that again sir...")
        listen()
        return None
    return query



def perform_tasks(query):
    if "aim" in query:
    
        speak('''The main objective of the Solar Tracking System project is to design 
and implement an effective tracking mechanism that adjusts the 
orientation of solar panels throughout the day. This system aims to 
increase energy capture by keeping the panels at an optimal angle 
to the sun, maximizing solar absorption and boosting overall energy 
output.
''')
        
    elif "sleep jarvis" in query:
        speak("bye sir have a good day, finally my work is finished after waiting for hours outside maam's cabin. you can call me anytime. thankyou")
        sys.exit()

    elif "components" in query:
        speak("1) 1 arduino uno 2) 1 servo motor 3) 2 light dependent resistors 4) 1 solar panel 5) 1 breadboard 6) 2 10k ohm resistors 7) some jumper wires")

    elif "circuit connection" in query:
        speak('''Set up two LDRs to detect sunlight intensity, which will help the Arduino determine the panel's movement.
For each LDR:
Connect one end of the LDR to 5V on the Arduino.
Connect the other end of the LDR to an analog pin on the Arduino (e.g., A0 for the first LDR and A1 for the second).
Connect a 10kΩ resistor between the Arduino GND and the analog input pin for each LDR. This creates a voltage divider circuit, allowing the Arduino to read light intensity.
Connect the control wire of the servo motor (usually yellow or white) to a PWM-capable digital pin on the Arduino (e.g., Pin 9).
Connect the power wire (red) of the servo motor to the 5V pin on the Arduino.
Connect the ground wire (black or brown) of the servo motor to GND on the Arduino.''')

    elif "logic" in query:
        speak(''' The logic behind your solar tracker system is centered on detecting the direction of sunlight using sensors (LDRs) and using a servo motor to adjust the solar panel’s angle to achieve optimal alignment with the sun.''')
    
    elif "picture" in query:
        cv2.imread
    
    elif "advantages" in query:
        speak('''The advantages of using a solar tracking system include: 
1) Maximizing energy output by aligning the panel with the sun.
2) Increasing the overall efficiency of solar panels by up to 25-30%.
3) Reducing the need for multiple fixed panels by optimizing one panel's output.''')

    elif "disadvantages" in query:
        speak('''Some disadvantages include:
1) Higher initial setup costs compared to fixed solar panels.
2) Requires regular maintenance due to moving parts.
3) May consume some power for the tracking mechanism itself.''')

    elif "threshold" in query:
        speak('''The threshold in the code is a value that determines when the system should adjust the solar panel’s position. 
If the difference between the light intensity readings of the two LDRs is greater than the threshold, the servo motor moves the panel. This helps avoid unnecessary movements due to small fluctuations in light.''')

    elif "what is an LDR" in query:
        speak('''An LDR, or Light Dependent Resistor, is a sensor that changes its resistance based on the light intensity. 
The Arduino uses this change in resistance to determine the brightness level detected by the LDR.''')

    elif "working principle" in query:
        speak('''The solar tracker works by using two LDRs to measure light intensity. The Arduino compares the readings from both LDRs. 
If one side receives more light, the servo motor moves the panel towards that direction to align with the sun.''')

    elif "efficiency" in query:
        speak('''The solar tracker increases the efficiency of the solar panel by adjusting its angle throughout the day to directly face the sun, thereby capturing more sunlight compared to a fixed panel.''')

    elif "how to improve" in query:
        speak('''To improve the solar tracking system, you could:
1) Add a second axis for better alignment.
2) Use more accurate sensors for higher precision.
3) Implement a rechargeable battery to store excess energy.''')
    elif "what is servo motor" in query:
        speak('''A servo motor is a type of motor that can be positioned at specific angles. It is controlled using PWM (Pulse Width Modulation) signals from the Arduino to rotate the solar panel to the optimal position based on the light intensity detected by the LDRs.''')

    elif "what is ldr" in query:
        speak('''An LDR (Light Dependent Resistor) is a type of resistor whose resistance decreases when exposed to light. It is used in the solar tracker system to detect the intensity of light falling on the solar panel. The Arduino uses the LDR readings to decide the position of the panel.''')

    elif "what is solar panel" in query:
        speak('''A solar panel is a device that converts light energy into electrical energy using photovoltaic cells. In the solar tracker system, it captures solar energy, and the system adjusts its angle to maximize energy absorption from the sun.''')

    elif "what is breadboard" in query:
        speak('''A breadboard is a tool used to build and test electronic circuits without the need for soldering. It allows you to connect components like the Arduino, LDRs, and the servo motor by inserting them into the board and connecting them with jumper wires.''')

    elif "what is resistor" in query:
        speak('''A resistor is a component that limits the flow of electrical current in a circuit. In the solar tracker system, resistors are used with the LDRs to form a voltage divider circuit, which helps the Arduino read the light intensity.''')

    elif "what is jumper wire" in query:
        speak('''A jumper wire is a short electrical wire used to make connections between components on a breadboard or circuit board. In the solar tracker system, jumper wires are used to connect the Arduino to the LDRs, servo motor, and other components.''')
    

    elif "who made you" in query:
        speak("I was developed by Manan Dudeja as part of the Group 5 project on solar tracking systems.")

    elif "how does servo motor work" in query:
        speak('''The servo motor receives signals from the Arduino to rotate to a specific angle. 
In the solar tracker, it adjusts the panel's angle based on the difference in light intensity detected by the LDRs.''')

    elif "sleep jarvis" in query:
        speak("Goodbye ma'am, have a good day. You can call me anytime. Thank you!")
        sys.exit()

    else:
        speak("I am not sure how to answer that. Please ask about the solar tracking system.")
        
def jarvis():
    wish()
    hour = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    sec = datetime.datetime.now().second
    speak("i am the chat bot made by manan dudeja for the project solar tracking system developed by group 5")

    speak(f"the time is currently {hour} hour {min} minutes {sec} seconds and now its the time to present you our project, if you have any doubt you can ask me anytime , i am always there to help")

    while True:
        query = listen().lower()

        
        perform_tasks(query)

jarvis()