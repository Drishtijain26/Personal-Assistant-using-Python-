import speech_recognition as sr
import webbrowser
import datetime
import os
import random
import ctypes
import time
import json
import subprocess
from urllib.request import urlopen
import pyjokes
import pyaudio
import wikipedia
import requests
import ecapture as ec

# Function to speak the text
def speak(text):
    print(text)
    # You can uncomment below lines and use pyttsx3 for TTS if needed
    # import pyttsx3
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()

# Function to wish based on the time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

# Function to send an email (placeholder implementation)
def sendEmail(to, content):
    # Implement email sending logic here
    pass

# Function to take voice commands
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
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    
    return query

# Main function
if __name__ == "__main__":
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    wishMe()
    intro = "Maya"  # Default name

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to YouTube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Overflow. Happy coding!")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\YourUsername\\Music"  # Update the path to your music directory
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No songs found in the directory")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open opera' in query:
            codePath = r"C:\\Path\\To\\Opera\\launcher.exe"  # Update the path to your Opera installation
            os.startfile(codePath)

        elif 'email to ishaan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver@example.com"  # Update with the actual recipient email
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Whom should I send it to?")
                to = input("Enter recipient email: ")  # Use input function to get recipient email
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, thank you")
            speak("How are you, Sir?")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            intro = query

        elif "change name" in query:
            speak("What would you like to call me, Sir?")
            intro = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(intro)
            print("My friends call me", intro)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you":
            speak("I have been created by Gaurav.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
            app_id = "Your_Wolframalpha_API_ID"  # Replace with your WolframAlpha API key
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely you're human.")

        elif "why you came to world" in query:
            speak("Thanks to the creator. Further, it's a secret.")

        elif 'power point presentation' in query:
            speak("Opening Power Point presentation")
            power = r"D:\Path\To\Presentation\file.pptx"  # Update the path to your PowerPoint file
            os.startfile(power)

        elif 'is love' in query:
            speak("It is the 7th sense that destroys all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by a human.")

        elif 'reason for you' in query:
            speak("I was created as a minor project by a human.")

        elif 'open bluestack' in query:
            appli = r"C:\\Path\\To\\BlueStacks\\Bluestacks.exe"  # Update the path to BlueStacks
            os.startfile(appli)

        elif 'news' in query:
            try:
                api_key = "Your_NewsAPI_Key"  # Replace with your NewsAPI key
                jsonObj = urlopen(f'https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey={api_key}')
                data = json.load(jsonObj)
                i = 1
                speak('Here are some top news from the Times of India')
                print('''=============== TIMES OF INDIA ============''' + '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'lock window' in query:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec! Your system is on its way to shut down")
            subprocess.call('shutdown /p /f')

        elif 'empty recycle bin' in query:
            import winshell
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("For how much time do you want to stop listening to commands?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "maya Camera", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown /h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the applications are closed before signing out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should I write, sir?")
            note = takeCommand()
            with open('maya.txt', 'w') as file:
                speak("Should I include date and time?")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            with open("maya.txt", "r") as file:
                content = file.read()
                print(content)
                speak(content)

        elif "maya" in query:
            wishMe()
            speak("Maya 1.0 in your service Mister")
            speak(intro)

        elif "weather" in query:
            api_key = "Your_OpenWeather_API_Key"  # Replace with your OpenWeather API key
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("City name?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(f"Temperature (in kelvin unit) = {current_temperature}\n"
                      f"Atmospheric pressure (in hPa unit) = {current_pressure}\n"
                      f"Humidity (in percentage) = {current_humidity}\n"
                      f"Description = {weather_description}")
            else:
                speak("City Not Found")

        elif "Good Morning" in query:
            speak("A warm " + query)
            speak("How are you?")
            speak(intro)

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about that, maybe you should give me some time")

        elif "i love you" in query:
            speak("But no one loves you")
