import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio
import random
import smtplib
import requests
from pprint import pprint
from selenium import webdriver
import playsound
from gtts import gTTS
import ssl
from PIL import Image
import subprocess
import pyautogui
import bs4 as bs
import urllib.request
import certifi


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
#print(voices[1].id)

engine.setProperty('voice', voices[1].id)

def there_exists(terms):
    for term in terms:
        if term in query:
            return True

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    speak("Welcome Sir")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good evening!")

    speak("CAN . at your service . please tell me how can i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query



r = sr.Recognizer()

def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chiragkng@gmail.com', '9045204516asdf')
    server.sendmail('chiragkng@gmail.com', to, content)
    server.close()




if __name__=="__main__" :
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "hello" in query or "hey" in query or "hi" in query:
            hel = "Hello sir ! How May i Help you.."
            print(hel)
            speak(hel)

        elif "your name" in query or "sweet name" in query:
            na_me = "Thanks for Asking my name my self ! CAN . what's your name?"  
            print(na_me)
            speak(na_me)

        if "my name is" in query:
            person_name = query.split("is")[-1].strip()
            speak("okay, i will remember that " + person_name)
            
            
        

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing! How are you', 'I am fine! , How are you', 'Nice!, How are you', 'I am nice and full of energy, How are you','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            
            if 'fine' in query or 'happy' in query or 'okey' in query:
                speak('okey..')  
            elif 'not' in query or 'sad' in query or 'upset' in query:
                speak('oh sorry..')

        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information CHIRAG YADAV Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)

        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am CAN an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        
        
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "show my routine" in query:
            im= Image.open(r"D:\IMAGES2\PROJECTS\AURDINO CAR")
            im.show()

        elif 'date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("sir, the date is")
            speak(date)
            speak(month)
            speak(year)

        elif 'game' in query:
            voice_data = record_audio("choose among rock paper or scissor")
            moves=["rock", "paper", "scissor"]
    
            cmove=random.choice(moves)
            pmove=voice_data
        

            speak("The computer chose " + cmove)
            speak("You chose " + pmove)
        #engine_speak("hi")
            if pmove==cmove:
                speak("the match is draw")
            elif pmove== "rock" and cmove== "scissor":
                speak("Player wins")
            elif pmove== "rock" and cmove== "paper":
                speak("Computer wins")
            elif pmove== "paper" and cmove== "rock":
                speak("Player wins")
            elif pmove== "paper" and cmove== "scissor":
                speak("Computer wins")
            elif pmove== "scissor" and cmove== "paper":
                speak("Player wins")
            elif pmove== "scissor" and cmove== "rock":
                speak("Computer wins")

        elif "plus" in query or "minus" in query or "multiply" in query or "divide" in query or "power" in query or "+" in query or "-" in query or "*" in query or "/" in query:
            
            opr = query.split()[1]

            if opr == '+':
                speak(int(query.split()[0]) + int(query.split()[2]))
            elif opr == '-':
                speak(int(query.split()[0]) - int(query.split()[2]))
            elif opr == 'multiply':
                speak(int(query.split()[0]) * int(query.split()[2]))
            elif opr == 'divide':
                speak(int(query.split()[0]) / int(query.split()[2]))
            elif opr == 'power':
                speak(int(query.split()[0]) ** int(query.split()[2]))
            else:
                speak("Wrong Operator")


        elif 'email to harry' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nehalsaxena28@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email") 

        elif 'weather' in query:
            query = query.replace("weather", "")
            webbrowser.open("https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5")
            speak("Here is what I found for on google")

        elif 'search in chrome' in query:
            speak("what should i search?")
            chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'


        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")  

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")    

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube") 

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google") 

        elif 'music from pc' in query or 'music' in query or 'gane chalao' in query:
            speak("ok i am playing music")
            music_dir = 'E:\\projects\\final yr. project\\music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,musics[-1]))

        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = 'E:\\projects\\final yr. project\\videos'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,videos[0]))  

  

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart") 

        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")

        

        

        elif 'good bye' in query:
            speak("good bye")
            exit()

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s') 

        elif query == 'none':
            continue 


        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()    





        
        
