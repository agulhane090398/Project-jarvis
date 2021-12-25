import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

from wikipedia.wikipedia import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir!")
    
    elif hour>= 12 and hour<18:
        speak("good afternoon sir!")

    else:
        speak("good evening sir!")

    speak("I am vaishali. Please tell me how can i help you?")


def takecommand():
    #to take input from user from microphone
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        

    try:
        print("Recognising.....")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server =  smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("aniketgulhane66@gmail.com","@NIKEtCUP98")
    server.sendmail("aniketgulhane66@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
        ##logic for task execution

        if 'wikipedia' in query:
            speak("Searching inwikipidea....")
            query=query.replace("wikipedia","")
            res = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(res)
            speak(res)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackover" in query:
            webbrowser.open("stackover.com")

        elif "play music" in query:
            music_dir = 'F:\\music\\new music'
            songs = os.listdir(music_dir)
            # print(songs)
            a=36
            os.startfile(os.path.join(music_dir,songs[a]))


        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(F"sir the time is {strtime}")

        elif "open visual studio" in query:
            codepath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "email to aniket" in query:
            try:
                speak("what should i say")
                content=takecommand()
                to = "aniketgulhane66@gmail.com"
                sendEmail(to,content)
                speak("email has been send!")
            except Exception as e:
                print(e)
                speak("sorry bhai email not send!")

        elif "exit" in query:
            speak("exiting sir!")
            exit()

