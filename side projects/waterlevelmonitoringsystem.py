import serial
import pyttsx3
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set up the serial communication with the Arduino
try:
    arduino = serial.Serial('COM7', 9600, timeout=1)  # Change 'COM3' to your Arduino port
   # time.sleep(2)  # Allow some time for the serial connection to initialize
    print("Connected to Arduino on port COM3")
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    exit()

# Function to make Jarvis speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Start monitoring the water level system
print("Jarvis is monitoring the water level...")

try:
    while True:
        if arduino.in_waiting > 0:
            # Read message from Arduino
            message = arduino.readline().decode('utf-8').strip()
            print(f"Received: {message}")

            # Respond based on the message received
            if "PUMP ON" in message:
                speak("The water pump is now on.")
            elif "PUMP OFF" in message:
                speak("The water pump is now off.")
            elif "TANK FULL" in message:
                speak("The water tank is full.")
            elif "No echo received" in message:
                speak("No echo received from the sensor.")
        
       # time.sleep(0.1)  # Small delay to prevent high CPU usage

except KeyboardInterrupt:
    print("\nProgram terminated by user.")

finally:
    # Close the serial connection when the program is terminated
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
        print("Serial connection closed.")
