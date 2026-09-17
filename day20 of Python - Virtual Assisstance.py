import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()
def speak(text):
    print('Assistant:',text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = take_command()
        print('You:',command)

    except sr.UnknownValueError:
        speak('Sorry,I could not understand you,')
        return ""
    except sr.RequestError:
        speak('Sorry recognition service is unavailable')
        return ""

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak('Good Morning!')
    elif hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('How can I help you?')

def run_assistant():
    wish_user()
    while True:
        command = take_command()

        if 'hello' in command:
            speak('Hello! How can i help you?')
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %S')
            speak(f'The current time is {current_time}')
        elif 'open youtube' in command:
            speak('Opening Youtube')
            webbrowser.open('https://www.youtube.com/')
        elif 'open google' in command:
            speak('Opening Google')
            webbrowser.open('https://www.google.com/')
        elif 'exit' in command or 'stop' in command:
            speak('Goodbye!')
            break
        else:
            speak("I don't know that command yet.")
run_assistant() 