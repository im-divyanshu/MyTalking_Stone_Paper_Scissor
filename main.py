import random
import pyttsx3
from playsound import playsound


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



speak("choos one from stone paper sceisor make sure enter correct spelling")
i=11
p=0
c=0
while(i>=1):
    i-=1
    print(f"chanses remaining {i+1}")
    speak(f"chanses remaining {i+1}")
    a=random.randint(1,3)
    if(a==1):
        comp="stone"
    if(a==2):
        comp="paper"
    if(a==3):
        comp="scisor"
    player=input("stone,paper,scisor : \n")

        
    if(comp=="stone"):
        if(player=="scisor"):
            print(f"computer choose {comp} you lose")
            speak(f"computer choose {comp} you lose")
            c+=1
        if(player=="paper"):
            print(f"computer choose {comp} you win")
            speak(f"computer choose {comp} you win")
            p+=1
    if(comp=="paper"):
        if(player=="stone"):
            print(f"computer choose {comp} you lose")
            speak(f"computer choose {comp} you lose")
            c+=1
        if(player=="scisor"):
            print(f"computer choose {comp} you win")
            speak(f"computer choose {comp} you win")
            p+=1
    if(comp=="scisor"):
        if(player=="paper"):
            print(f"computer choose {comp} you lose")
            speak(f"computer choose {comp} you lose")
            c+=1
        if(player=="stone"):
            print(f"computer choose {comp} you win")
            speak(f"computer choose {comp} you win")
            p+=1

    if(player==comp):
        print(f"computer choose {comp} its a tie")
        speak(f"computer choose {comp} its a tie")
        p+=1
        c+=1
    print(f"                                computer point [{c}] your point [{p}]")
    speak(f"computer point [{c}] your point [{p}]")
if(p==c):
    print("it is a tie")
    speak("it is a tie")
if(p>c):
    print("yeh you defeated computer winner ")
    speak("yeh you defeated computer winner ")
else:
    print("oh you are defeated by the computer ")
    speak("oh you are defeated by the computer ")
