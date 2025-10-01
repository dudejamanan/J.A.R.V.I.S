import random
import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate",150)
engine.setProperty("volume",0.9)

voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)


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