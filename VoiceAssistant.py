import pyttsx3 
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser
from bs4 import BeautifulSoup
import os
from datetime import timedelta, datetime
from pygame import mixer
from plyer import notification
import speedtest
from keyboard import volume_up, volume_down
import random
import requests

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message")
    a = int(input('''Person 1 - 1
    Person 2 - 2'''))
    if a == 1:
        speak("What's the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+91000000000", message, time_hour=strTime, time_min=update)
    elif a == 2:
        pass

elif "shutdown the system" in query:
    speak("Are You sure you want to shutdown")
    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
    if shutdown == "yes":
        os.system("shutdown /s /t 1")
    elif shutdown == "no":
        break

elif "schedule my day" in query:
    tasks = []  # Empty list
    speak("Do you want to clear old tasks (Plz speak YES or NO)")
    query = takeCommand().lower()
    if "yes" in query:
        file = open("tasks.txt", "w")
        file.write(f"")
        file.close()
        no_tasks = int(input("Enter the no. of tasks :- "))
        for i in range(no_tasks):
            tasks.append(input("Enter the task :- "))
            file = open("tasks.txt", "a")
            file.write(f"{i}. {tasks[i]}\n")
            file.close()
    elif "no" in query:
        i = 0
        no_tasks = int(input("Enter the no. of tasks :- "))
        for i in range(no_tasks):
            tasks.append(input("Enter the task :- "))
            file = open("tasks.txt", "a")
            file.write(f"{i}. {tasks[i]}\n")
            file.close()

elif "show my schedule" in query:
    file = open("tasks.txt", "r")
    content = file.read()
    file.close()
    mixer.init()
    mixer.music.load("notification.mp3")
    mixer.music.play()
    notification.notify(
        title="My schedule :-",
        message=content,
        timeout=15
    )

elif "open" in query:  # EASY METHOD
    query = query.replace("open", "")
    query = query.replace("jarvis", "")
    pyautogui.press("super")
    pyautogui.typewrite(query)
    pyautogui.sleep(2)
    pyautogui.press("enter")

elif "internet speed" in query:
    wifi = speedtest.Speedtest()
    upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
    download_net = wifi.download() / 1048576
    print("Wifi Upload Speed is", upload_net)
    print("Wifi download speed is ", download_net)
    speak(f"Wifi download speed is {download_net}")
    speak(f"Wifi Upload speed is {upload_net}")

elif "ipl score" in query:
    url = "https://www.cricbuzz.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
    team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
    team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
    team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

    a = print(f"{team1} : {team1_score}")
    b = print(f"{team2} : {team2_score}")

    notification.notify(
        title="IPL SCORE :- ",
        message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
        timeout=15
    )