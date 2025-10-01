import pyttsx3 #module for text to speech (speaking to user)
import speech_recognition as sr #module for speech to text (listening user) (as sr isliye likha ki itni badi spelling baar baar kon likhega)
#for using microphone i installed pyaudio too 
import datetime #to get current time
import os #for opening files
import sys
import cv2 #module for video capture 
from requests import get 
import wikipedia #module used to access data from youtube
import webbrowser #for opening websites
import pywhatkit #for sending whatsapp messages , for playing songs on youtube
import smtplib
import pyjokes
import pygame
import random
import pyautogui #module to control mouse , keyboard and other gui automation tasks
import time
import instaloader
import PyPDF2


engine = pyttsx3.init('sapi5') #initailising module
voices = engine.getProperty('voices') #getting voices as a list
engine.setProperty("rate",200) #setting the voice rate
engine.setProperty('voice',voices[0].id) #setting one voice in a list(it has 2 voices by default , for index 0 and 1)
print(voices[0].id) #this prints the id the voice

#text to speech
def speak (audio): #creating a function for text to speech 
    engine.say(audio) 
    print(audio)
    engine.runAndWait() #it runs the voice and waits till the voice ends

def listen():
    r= sr.Recognizer() #this processes the audio to text
    with sr.Microphone() as source: #with command automatically closes the microphone after use
        print("listening...")
        r.pause_threshold = 1 #it means the program will wait for how much seconds before it stops listening
        audio = r.listen(source,timeout = 5, phrase_time_limit = 10) #timeout means it will wait 1 second for user to start listening
        #phrase_time_limit means ki kitne time ke liye it will listen
    while True:
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

def wish():
    hour = int(datetime.datetime.now().hour) #this prints hour of abhi ka time in int
    min = int(datetime.datetime.now().minute)
    if hour>=0 and hour<=12:
        speak("good morning sir.")
    elif hour>12 and hour<16:
        speak("good afternoon sir.")
    else:
        speak("good evening sir.")
    a=0
    if hour>=0 and hour<=12:
        a="AM"
    
    else:
        a="PM"
    
    speak(f'''its {hour}:{min} {a}
and you are late for work as usual''')

def pdf_reader():
    book = open("C://Users//Manan//Downloads//BMGT107L_BUSINESS-ANALYTICS_TH_1.0_0_BMGT107L.pdf","rb")#opening the file in binary (rb is read binary)
    pdfreader = PyPDF2.PdfReader(book) 
    pages = len(pdfreader.pages)
    speak(f"total number of pages in the book are {pages}")
    speak("please sir enter the page number i have to read")
    pg = int(input("please enter the page number:"))
    speak("what should be the speed limit of the text")
    speed_text = int(input("enter speed: "))
    engine.setProperty("rate",speed_text)



    page = pdfreader.pages[pg] #assigning a variable to the text of page number: pg
    text=page.extract_text() #getting the text in variable text
    speak(text)
    engine.setProperty("rate",150)



def perform_tasks(query):

        #logic building for tasks

    if "open notepad" in query:
        notepad_path = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(notepad_path)
    
    elif "close notepad" in query:
        speak("okay sir closing notepad")
        os.system("taskkill /f /im notepad.exe") #taskkill i a windows command used to terminate tasks
        #/f flag forces the termination of tasks
        #/im specifies the image name(in this case notepad.exe)

    
    elif "tell a joke" in query:
        a= pyjokes.get_joke()
        speak(f"{a}")
        speak("do you want to hear another sir")
        

    elif "set an alarm" in query:
       
        speak("okay sir , what should be the hour?")
        query_hour=int(listen())
        speak("and what should be the minutes")
        query_min = int(listen())
        while True:
            current_hour = int(datetime.datetime.now().hour)
            current_min = int(datetime.datetime.now().min)
            if current_hour == query_hour and current_min ==query_min:
                speak("wake up sir")

        
    elif "open cmd" in query:
        os.system("start cmd")

    elif "hear" in query:
        speak("yes i can listen you sir")

    elif "sleep jarvis" in query:
        speak("bye sir have a good day, you can call me anytime , at night too")
        sys.exit()
        
    elif "open camera" in query:
        cap = cv2.VideoCapture(0) #opens a connection to default webcam (camera 0) #cap is the video capture object
        while True: #purpose of this loop is to continously capture frames and display
            ret , img = cap.read() #reads a frame from video capture object #ret is a boolean indicating frame was successfully captured (true from successful)
            #img = photo , frame captured from the webcam
            cv2.imshow("webcam",img) 
            k = cv2.waitKey(50) #each frame before displaying waits for 50 mili seconds if any key is pressed , it returns ascii value of the key pressed
            if k == 27: #if ascii value of esc is 27 , so if esc is pressed it breaks
                break
        cap.release() #releases webcam so that other applications can access it
        cv2.destroyAllWindows() #closing all cv windows opened by program

    elif "ip address" in query:
        ip = get("https://api.ipify.org").text
        speak(f"your ip address is {ip}")
        query = listen().lower()
        if "repeat" in query:
            speak(f"your ip address is {ip}")
            
    elif "wikipedia" in query:
        speak("searching wikipedia...")
        query = query.replace("wikipedia","")#query mei se wikipedia word htare hai taaki voh "wikipedia" word ka result show na kre
        speak("According to wikipedia")
        results = wikipedia.summary(query , sentences = 2)
        speak (results)
        
    elif "open youtube" in query:
        webbrowser.open("www.youtube.com")

    elif "open instagram" in query:
        webbrowser.open("www.instagram.com")

    elif "thankyou" in query:
        speak("no problem sir ")

    elif "open whatsapp" in query:
        webbrowser.open("web.whatsapp.com")

    elif "monkey type" in query:
        webbrowser.open("www.monkeytype.com")
        
    elif "open facebook" in query:
        webbrowser.open("www.facebook.com")
        
    elif "open google" in query:
        speak("what may i search on google sir?")
        query = listen().lower()
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "send message" in query:
        pywhatkit.sendwhatmsg("+918595115309","this message has been sent by jarvis",13,16)
        
    elif "play song" in query:

        speak("what song would you like to listen sir")
        query = listen().lower()
        speak(f"playing {query}")
        pywhatkit.playonyt(f"{query}")
        
    elif "who am i " in query:
        speak("dont you even know who you are? bro you are manan dudeja okay please remember else your life will be in darkness")
    
    elif "shutdown the system" in query:
        os.system("shutdown /s /t 5")
        #/s shuts down the computer
        # /t 5 delays the shutdown by 5 seconds

    elif "restart the system" in query:
        os.system("shoutdown /r /t 5")

    elif "play snake game" in query:
        pygame.init()

        #colors
        white = (255,255,255) 
        red = (255,0,0) 
        black = (0,0,0) 


        screen_width = 600
        screen_height = 600

        #creating window
        gameWindow = pygame.display.set_mode((screen_width,screen_height))

        #game title
        pygame.display.set_caption("ohmysnake")
        pygame.display.update()


        clock = pygame.time.Clock() 

        font = pygame.font.SysFont(None,50) 

        def text_screen(text,color,x,y):  
            screen_text = font.render(text,True,color) 
            gameWindow.blit(screen_text,[x,y]) 

        def plot_snake(gameWindow,color,snk_list,snake_size):
            for x,y in snk_list:
                pygame.draw.rect(gameWindow,color, [x,y,snake_size,snake_size])
            



        def game_loop():
            
            #game specific variables
            exit_game = False
            game_over = False
            snake_x= 45
            snake_y = 55
            snake_size = 12
            fps = 60
            velocity_x = 0
            velocity_y = 0
            food_x= random.randint(20,screen_width-20)
            food_y = random.randint(20,screen_height-20) 
            foodsize = 12
            init_velocity = 10
            score = 0

            snk_list = [] 
            snk_length = 1 

            #game loop 
            while not exit_game:
                if game_over:
                    gameWindow.fill(white)
                    text_screen("game over! press enter to continue",red,10, 270)
                    for event in pygame.event.get():
                    
                        if event.type == pygame.QUIT: 
                            exit_game = True 
                            
                        if event.type == pygame.KEYDOWN: 
                            game_loop()

                else:
                    for event in pygame.event.get():
                    
                        if event.type == pygame.QUIT:
                            exit_game = True
                    
                        if event.type == pygame.KEYDOWN: 
                            if event.key == pygame.K_RIGHT:
                                velocity_x = init_velocity
                                velocity_y = 0
                            if event.key == pygame.K_LEFT:
                                velocity_x = -init_velocity
                                velocity_y = 0
                            if event.key == pygame.K_UP:
                                velocity_y = -init_velocity
                                velocity_x = 0
                            if event.key == pygame.K_DOWN:
                                velocity_y = init_velocity
                                velocity_x = 0
                
                    snake_x= snake_x + velocity_x 
                    snake_y = snake_y + velocity_y 
                
                    if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                        score+=1
                        print("score is", score)
                        food_x= random.randint(20,screen_width-20)
                        food_y = random.randint(20,screen_height-20) 
                        snk_length+=5


                    gameWindow.fill(red)
                    text_screen("score: "+str(score*10),black,5,5)
                

                    head = [] 
                    head.append(snake_x)
                    head.append(snake_y)
                    snk_list.append(head) 

                    if len(snk_list)>snk_length: 
                        del snk_list[0]

                    if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                        game_over = True

                    if head in snk_list[:-1]:
                        game_over = True  

                    pygame.draw.rect(gameWindow,white,[food_x,food_y,foodsize,foodsize]) 

                    plot_snake(gameWindow,black,snk_list,snake_size)

                pygame.display.update()
                clock.tick(fps)
            pygame.quit()
            
        game_loop()
    
    elif "play snake water game" in query:
        engine.say("hello welcome to manan's developed audio snake water gun game ,tho you have to still type your response lol, so without wasting time let's get started")
        engine.runAndWait()

        a = ["snake", "water" , "gun"]
        b=random.choice(a)
        engine.say("choose snake water gun")
        engine.runAndWait()
        c= input("choose snake water gun")
        engine.say(f"so you chose{c}")
        engine.runAndWait()

        print("computer chose" , b)
        engine.say(f"and computer chose {b}")
        engine.runAndWait()


        if c==b:
            print("its a tie")
            engine.say("hence its a tie")
            engine.runAndWait()

        if c=="snake" and b=="water":
            print("you win")
            engine.say("snake drank the water and you win")
            engine.runAndWait()

        elif c=="snake" and b=="gun":
            print("u loose")
            engine.say("gun shot the snake and you loose")
            engine.runAndWait()

        elif c=="gun" and b =="snake":
            print("u win")
            engine.say("gun shot the snake and you win")
            engine.runAndWait()

        elif c=="gun" and b =="water":
            print("u loose")
            engine.say("gun got drown in water and you loose")
            engine.runAndWait()

        elif c=="water" and b =="gun":
            print("you win")
            engine.say("gun got drown in water and you win")
            engine.runAndWait()

        elif c=="water" and b =="snake":
            print("you loose")
            engine.say("snake drank the water and you loose")
            engine.runAndWait()
    
    elif "sleep the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
    elif "switch the window" in query:
        pyautogui.keyDown("alt") #alt dbaya
        pyautogui.press("tab") #tab press kra
    
        pyautogui.keyUp("alt") #alt chorda

    elif "take screenshot"  in query:
        speak("sir, please tell the name for this screenshot file")
        name=listen().lower()
        speak("sir , please hold the screen for few seconds , i am taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("i am done sir , the screenshot is saved in our main folder. now i am ready for another work")

    elif "copy text" in query:
        pyautogui.keyDown("ctrl")
        pyautogui.press("c")
        pyautogui.keyUp("ctrl")
        time.sleep(2)
        speak("text is successfully copied")
    
    elif "paste text" in query:
        pyautogui.keyDown("ctrl")
        pyautogui.press("v")
        pyautogui.keyUp("ctrl")
        speak("text is successfully pasted")

    elif "instagram profile" in query:
        speak("sir input the username correctly")
        name=input("input username:")
        webbrowser.open(f"www.instagram.com/{name}")
        speak(f"sir here is the profile of user {name}")
        time.sleep(3)
        speak("sir , would you like to download the instagram profile of this user?")
        time.sleep(2)
        query=listen().lower()
        if "yes" in query:
            mod = instaloader.Instaloader()
            mod.download_feed_posts(name)
            speak("the profile picture is saved in our main folder. now i am ready ")
        else:
            pass

    elif "where are we" in query:
        speak("wait sir , let me check")
        try:
            ipAdd= get("http://api.ipify.org").text
            print(ipAdd)
            url= "https://get.geojs.io/v1/ip/geo/"+ipAdd+".json"
            geo_requests=get(url)
            geo_data = geo_requests.json()
            city = geo_data['city']
            state = geo_data['state']
            country = geo_data['country']
            speak(f"we are in {city} city of {state} of {country} ")
        except Exception as e:
            speak("sorry sir , due to network issue i am not able to find out our location")

    elif "change speed" in query:
        speak("what should be my speed sir?")
        speed = int(input("enter speed: "))
        engine.setProperty("rate",speed)
        speak(f"speed changed to {speed}")

    elif "change volume" in query:
        speed("what should be my volume sir?")
        volume = float(input("enter volume (between - to 1): ")) 
        engine.setProperty("volume",volume)
        speak(f"volume changed to {volume}")   

    elif "read pdf" in query:
        pdf_reader()

    elif "hide files" in query:
        os.system("attrib +h /s /d") #+h means hide
        speak("sir, all files are now hidden")
    
    elif "unhide files" in query:
        os.system("attrib -h /s /d") #-h means unhide
        speak("sir all files are now visible to everyone")



    else:
        return False
    return True

def jarvis():
    wish()
    
    
    
    

    #speak(f"the time is currently {hour} hour {min} minutes {sec} seconds and you are late for work as usual")
    
    while True:
        query = listen().lower()

        
        perform_tasks(query)

           

jarvis()

