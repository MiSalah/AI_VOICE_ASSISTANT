import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def saygood():
    hour = datetime.datetime.now().hour
    
    if hour > 5 and hour <=12:
        speak("Good Morning")
    elif hour > 12 and hour <= 18:
        speak("Good afternoon")
    elif hour >18 and hour <=24:
        speak("Good evening")
    else:
        speak("Good Night")
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    saygood()
    speak("The current date is")
    speak(year)
    speak(month)
    speak(day)

    
def greetings():
    speak("Welcome Back Sir")
    date()
    speak("See you soon")

def VoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ... ")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:       
        print("Recognising...")
        query = r.recognize_google(audio,language = 'en')
        
    except Exception as e:
        print("Error :  " + str(e))
        speak("Repeat the speech again")
        return "None"

    with open("recorded.wav", "wb") as f:

        f.write(audio.get_wav_data())
    
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp@gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("elbaidoury.user@gmail","******")
    server.sendmail("elbaidoury.user@gmail.com",to,content)
    server.close()


if __name__ == "__main__":
    
    greetings()
    
    while True:
        query = VoiceCommand().lower()
        print(query)
        if "hello" in query:
            saygood()
        elif "date" in query:
            saygood()
            date()
        elif "offline" in query: 
            quit()        
        elif "goodbye" in query:
            speak("Thank You, See you soon again!")
            quit()
        elif "google" in query:
            speak("searching ...")
            query = query.replace("google","")
            result = wikipedia.summary(query,sentences = 2)
            speak(result)
        elif "send email" in query:
            emails = {   
                "elbaidoury":"elbaidoury.salaheddine@gmail.com",
                "shop":"elbaidoury.shop@gmail.com",
                "course":"elbaidoury.course@gmail.com"
            }
            
            try:
                speak("What should i say !")
                content = VoiceCommand().lower()
                print(content)
                speak("what is the receiver email")
                to = VoiceCommand().lower()
                print(to)
                sendEmail(emails[to],content)
                speak("email sent successfully to"+emails[to])
            
            except Exception as e:
                print(e)
                speak("enable to send the mail")