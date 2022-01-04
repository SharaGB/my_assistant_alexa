import pyttsx3 # Tranformar el texto a una voz sintética
import speech_recognition as txt # Pasar de audio a texto
import subprocess as sub
from datetime import datetime

voice = pyttsx3.init() # Inicializar

# Obetener la lista de voces y establecerla
get_voices = voice.getProperty('voices') # Obtener lista de todas las voces disponibles
voice.setProperty('voice', get_voices[0].id) # Configurar la propiedad de la voz

# Configuración de voz
voice.setProperty('rate', 150)
voice.setProperty('volume', 0.8)

voice.say('¿Ahora qué quiere?') # Dice el texto que le ingresamos
voice.runAndWait()

def talk(text):
    voice.say(text)
    voice.runAndWait()

while True:
    # Reconocer la voz
    listener = txt.Recognizer()
    # Activar micrófono
    with txt.Microphone() as src:
        print("Escuchando...")
        audio = listener.listen(src, phrase_time_limit=5) # Escucha el micrófono

    try:
        reco = listener.recognize_google(audio)
        print(reco)

        reco = reco.lower()
        reco = reco.split(' ')

        # Name of the my assistant
        if 'Sylvanas' in reco:
            if 'abre' in reco or 'abrir' in reco:
                sites = {
                    'google': 'google.com',
                    'youtube': 'youtube.com',
                    'instagram': 'instagram.com',
                    'twitter': 'twitter.com'
                }

                for x in list(sites.heys()):
                    if x in reco:
                        sub.call(f'start chrome.exe {sites[x]}', shell=True)
                        talk(f'Abriendo {x}')

            elif 'hora' in reco:
                time = datetime.now().strftime('%H:%M')
                talk(f'Son las {time}')

            for i in ['termina', 'terminar', 'terminó']:
                if i in reco:
                    talk(f'Goodbye')
                    break

    except:
        print ("No te entendí, por favor vuelve a intentar")
