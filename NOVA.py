import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime 
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speechtx("listening")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            speechtx("recognizing")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not understood")
            speechtx("not understood")
            time.sleep(2)
            return sptext()

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        speechtx("Hello, I am NOVA. Let's start")
        data1 = sptext().lower()

        if "your name" in data1:
            name = "My name is NOVA"
            speechtx(name)
            continue

        elif "old are you" in data1:
            age = "I am two years old"
            speechtx(age)
            continue

        elif 'time' in data1:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speechtx("The time is " + time_now)
            continue

        elif 'youtube' in data1:
            speechtx("Opening WsCube Tech YouTube channel")
            webbrowser.open("https://www.youtube.com/c/wscubetechjodhpur")

        elif 'web' in data1:
            speechtx("Opening WsCube Tech website")
            webbrowser.open("https://www.wscubetech.com/")

        elif "joke" in data1:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke_1)
            speechtx(joke_1)
            continue

        elif 'play song' in data1:
            speechtx("Do you want to play a system song or YouTube song?")
            ask = sptext().lower()

            if "youtube" in ask:
                webbrowser.open("https://www.youtube.com/watch?v=DyKjsL-6-Z8&ab_channel=jackson")
            elif ("song" in ask) or ("folder" in ask):
                try:
                    add = "D:\\gaurav\\song"
                    listsong = os.listdir(add)
                    print(listsong)
                    os.startfile(os.path.join(add, listsong[1]))
                except:
                    speechtx("No songs found in the folder")
                    continue
            else:
                speechtx("Wrong command")
                continue

        elif ("exit" in data1) or ("stop" in data1):
            speechtx("Thank you. Goodbye from NOVA.")
            break
        else:
            speechtx("Wrong command")
            continue

        time.sleep(5)
