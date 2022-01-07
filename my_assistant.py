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
voice.setProperty('voice', get_voices[2].id) # Configurar una propieda dentro de voice

# Configuración de voz
voice.setProperty('rate', 130)
voice.setProperty('volume', 1.5)

voice.say('¿Ahora qué quiere?')
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
        if "cortana" in command:
            command = command.replace('cortana', '')

        return command
    except:
        talk("Por favor vuelve a intentar")
        return ("Falló")

def run():
    command = listen()

    if 'reproduce' in command or 'reproducir' in command:
        music = command.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)

    elif 'abre' in command or 'abrir' in command:
        sites = {
            'google': 'google.com',
            'youtube': 'youtube.com',
            'instagram': 'instagram.com',
            'twitter': 'twitter.com'
            }
        for x in list(sites.keys()):
            if x in command:
                sub.call(f'start chrome.exe {sites[x]}', shell=True)
                talk('Abriendo' + x)

    elif 'hora' in command or 'horas' in command:
        time = datetime.now().strftime('%I:%M %p')
        talk('Son las ' + time)

    elif "busca" in command or "buscar" in command:
        search = command.replace('busca', '')
        if len(search) <= 5:
            print("No se encontró nada")
        else:
            wiki = wikipedia.summary(search, 1)
            talk(wiki)

    if 'adiós' in command or 'adios' in command or 'salir' in command:
        talk('Hasta pronto')
        os._exit(1)

while True:
    run()
