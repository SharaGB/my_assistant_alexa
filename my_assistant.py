import pyttsx3 # Tranformar el texto a una voz sintética
import speech_recognition as txt # Pasar de audio a texto
import subprocess as sub
import pywhatkit
import wikipedia
import os
from datetime import datetime

listener = txt.Recognizer()

voice = pyttsx3.init() # Inicializar

# Obetener la lista de voces y establecerla
get_voices = voice.getProperty('voices') # Obtener lista de todas las voces disponibles
voice.setProperty('voice', get_voices[1].id) # Configurar una propieda dentro de voice

# Configuración de voz
voice.setProperty('rate', 130)
voice.setProperty('volume', 1.5)

voice.say('Welcome!')
voice.runAndWait()

def talk(text):
    voice.say(text)
    voice.runAndWait()

def listen():
    with txt.Microphone() as src: # Activar micrófono
        print("Escuchando...")
        audio = listener.listen(src, phrase_time_limit=3) # Escucha el micrófono
    try:
        command = listener.recognize_google(audio) # Obetener el método de Google
        print(command)

        command = command.lower()
        if "Isis" in command:
            command = command.replace('Isis', '')

        return command
    except:
        talk("Please try again")
        return ("Falló")

def run():
    command = listen()

    if 'plays' in command:
        music = command.replace('plays', '')
        talk('Playing ' + music)
        pywhatkit.playonyt(music)

    elif 'open' in command or 'opens' in command:
        sites = {
            'google': 'google.com',
            'youtube': 'youtube.com',
            'instagram': 'instagram.com',
            'twitter': 'twitter.com',
            'facebook': 'facebook.com'
            }
        for x in list(sites.keys()):
            if x in command:
                sub.call(f'start chrome.exe {sites[x]}', shell=True)
                talk('Opening' + x)

    elif 'time' in command or 'hour' in command:
        time = datetime.now().strftime('%I:%M %p')
        talk('It is ' + time)

    elif "search" in command:
        search = command.replace('search', '')
        if len(search) <= 5:
            print("I don't know found anything")
        else:
            wiki = wikipedia.summary(search, 1)
            talk(wiki)

    if 'bye' in command or 'adios' in command or 'adiós' in command:
        talk('See you soon')
        os._exit(1)

while True:
    run()
