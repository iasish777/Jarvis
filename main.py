import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open x" in c:  # Assuming 'x' is a placeholder for some site
        webbrowser.open("https://x.com")

if __name__ == '__main__':
    speak("Hey Sir, I am your Assistant. I am here to help you.")

    recognizer = sr.Recognizer()
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)

                if word.lower() == "jarvis":
                    speak("Yes sir.")
                    # Add what you want to do when "Jarvis" is recognized
                    with sr.Microphone() as source:
                        print("Jarvis Active")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        process_command(command)

        except Exception as e:
            print("Sorry I didn't understand that")