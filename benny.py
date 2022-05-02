import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser as wb

benny = pyttsx3.init()
voice = benny.getProperty('voices')
benny.setProperty('voices', voice[0].id)

benny.setProperty("rate", 175)
benny.runAndWait()


def speak(audio):
    print('Benny: ' + audio)
    benny.say(audio)
    benny.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak("It is " + Time)


def welcome():
    hour = datetime.datetime.now().hour
    if 6 < hour < 12:
        speak("Good morning sir!")
    elif 12 < hour < 20:
        speak("Good evening sir!")
    elif 20 < hour < 24:
        speak("Good night sir!")


def Qhelp():
    import random
    number = random.randint(1, 4)
    speak("I'm benny")
    if number == 1:
        speak("How can I help you sir?")
    if number == 2:
        speak("Are you calling me sir?")
    if number == 3:
        speak("Do you need any help sir?")
    if number == 4:
        speak("I'm here to help you sir!")


def command():
    c = sr.Recognizer()
    with sr.Microphone() as mic:
        c.pause_threshold = 2
        audio = c.listen(mic)
    try:
        query = c.recognize_google(audio, language='en')
        print("Bill: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input("Your order is: "))
    return query


if __name__ == '__main__':
    welcome()
    Qhelp()

    while True:
        query = command().lower()
        if 'google' in query:
            speak("What do you want to know sir?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'here is your {search} on google')
        query = command().lower()
        if 'youtube' in query:
            speak("What do you want to watch sir?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'here is {search} on youtube')
        elif "time" in query:
            time()
        elif "exit" in query:
            speak("Have a good day sir, Benny is shutting down!")

