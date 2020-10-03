import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hey Jason this side   How can I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  


    except Exception:
        
        print("Say that again please...")  
        return "None" 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    #while True:
    if 1:
        query = takeCommand().lower() 
        
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how can I help you?')
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open spotify' in query:
            webbrowser.open("open.spotify.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        
        elif 'play music' in query:
            music_dir = 'D:\\MOVIES'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        elif 'visual studio' in query:
            codePath = "C:\\Users\\hriti\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am really sorry. I am not able to send this email")
                
        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timer_time = takeCommand()
            timer_time = timer_time.replace('minutes', '')
            timer_time = timer_time.replace('minute', '')
            timer_time = timer_time.replace('for', '')

            timer_time = float(timer_time)
            timer_time = timer_time * 60
            speak(f'I will remind you in {timer_time} seconds')

            time.sleep(timer_time)
            speak('Your time has been finished sir')
        
        elif 'bye' in query:
            speak('Have a great time, bye')
           #comments
