import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime


speaker = win32com.client.Dispatch("Sapi.SpVoice")



def say(text):
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said:{query}")
            return query
        except Exception as e:
            return "Some error occurred, sorry for the inconvenience"


if __name__ == "__main__":
    print("Jarvis Speaking")
    say("Hello sir, I'm Jarvis, how may I help you today?")
    print("Listening...")
    while True:
        query = takeCommand()

        #you can add more sites here:
        sites = [["YouTube", "https://www.youtube.com"], ["Twitter", "https://www.twitter.com"],["Google", "https://www.google.com"], ["Reddit", "https://www.reddit.com"], ["Facebook", "https://www.facebook.com"], ["Github", "https://www.github.com"], ["Instagram", "https://www.instagram.com"], ["Hacker Rank", "https://www.hackerrank.com/dashboard"], ["Spotify", "https://open.spotify.com"], ["Wikipedia", "https://www.wikipedia.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                break

                #you can add more music here:
            if "Play Music".lower() in query.lower():
                musicPath = "E:\Jarvis\music\west-side.mp3"
                os.system(f"start {musicPath}")
                break

            if "The Time".lower() in query.lower():
                time = datetime.datetime.now().strftime("%I:%M %p")
                say(f"Sir the time is {time}")
                break





        #say(query)
