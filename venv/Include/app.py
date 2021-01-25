import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        talk("Говорите ")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio).lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("не понял")
        zadanie = command()

    return zadanie

def makeSomething(zadanie):
    if 'open website' in zadanie:
        talk("ok")
        url = 'https://vk.com'
        webbrowser.open(url)
    elif 'stop' in zadanie:
        talk("Закрываюсь")
        sys.exit()
    else:
        talk("еще раз")

while True:
    makeSomething(command())