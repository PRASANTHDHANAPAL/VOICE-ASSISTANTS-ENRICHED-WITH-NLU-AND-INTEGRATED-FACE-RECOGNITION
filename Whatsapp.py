import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.datetime.now().strftime("%H"))
update = int((datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message, Person 1 or Person 2?")
    person_choice = takeCommand().lower()
    
    if "person one" in person_choice:
        speak("What's the message for Person one?")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+91 86084 13156", message, time_hour=strTime, time_min=update)
    elif "person two" in person_choice:
        speak("What's the message for Person two?")
        message = takeCommand()
        
        pywhatkit.sendwhatmsg("+91000000000", message, time_hour=strTime, time_min=update)
    else:
        speak("Invalid choice. Please try again.")

if __name__ == "__main__":
    sendMessage()