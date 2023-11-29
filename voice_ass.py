import datetime
from datetime import datetime as dt
import speech_recognition as sr
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',200)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing the background noices..Please Wait!")
        recognizer.adjust_for_ambient_noise(source, 0.3)
        print("Ask me anything.....")
        recordedauio=recognizer.listen(source)

    try:
        text=recognizer.recognize_google(recordedauio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

        def wishme():
            hour=int(datetime.datetime.now().hour)
            if hour>0 and hour<12:
                return(" Good Morning")
            elif hour>=12 and hour<16:
                return("Good Afternoon ")
            else:
                return("Good Evening ")


        if 'hello' in text:
                msg="Hello... "+wishme()+ "....I am your personal assistant.. ask me anything"
                engine.say(msg)
                engine.runAndWait()


        if 'browser' in text:
                a='Opening Browser...'
                engine.say(a)
                engine.runAndWait()
                program="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
                subprocess.Popen([program])

        if 'date and time' in text:
                date = dt.now()
                format_date = date.strftime("%B %d, %Y")
                time = dt.now()
                format_time = time.strftime("%I:%M")
                print(format_date)
                print(format_time)
                format_date="Today's date is.."+format_date+"....and time is.."+format_time+".."
                engine.say(format_date)
                engine.runAndWait()


        if 'play' in text:
                a="Opening Youtube.."
                engine.say(a)
                engine.runAndWait()
                pywhatkit.playonyt(text)
        if 'youtube' in text:
                a="Opening Youtube.."
                engine.say(a)
                webbrowser.open("www.youtube.com")
                engine.runAndWait()

        if 'exit' in text:
                txt="Thank you! bye"
                engine.say(txt)
                engine.runAndWait()
                engine.stop()



    except Exception as ex:
        print(ex)

    
while True:
     cmd()
