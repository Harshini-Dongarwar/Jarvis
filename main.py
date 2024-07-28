import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary
import requests
from openai import OpenAI
r = sr.Recognizer()
engine = pyttsx3.init()
newsApi='914398da85824f83b0a3c1d2b52efa52'

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command):
    client = OpenAI( api_key="sk-proj-MYzWe2zVkgSnNP1iYI3nT3BlbkFJqBP6ZWunZG21uHSaUysT",
 
)
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
    {"role": "system", "content": "You are a Virtual assistant named Jarvis, skilled in general tasks Alexa and Google cloud."},
    {"role": "user", "content": command}
  ]
)
    return completion.choices[0].message.content
    

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=914398da85824f83b0a3c1d2b52efa52')
        if r.status_code==200:
            data=r.json()
            articles=data.get('articles',[])
            for article in articles:
                speak(article['title'])
    else:
        output=aiProcess(c)
        speak(output)
                    
 
if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        with sr.Microphone() as source:
            print("Listening!")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                print("Recognizing...")
                word = r.recognize_google(audio)
                print(f"Heard: {word}")
                if word.lower() == "jarvis":
                    speak("Yes?")
                    
                    # Listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Active")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        print(f"Command: {command}")
                        processCommand(command)
                        speak("Command executed")
            
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Recognition error: {e}")
            except Exception as e:
                print(f"Error: {e}")
