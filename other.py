import pyttsx3 # Tranformar el texto a una voz sintética
import speech_recognition as txt # Pasar de audio a texto
import subprocess as sub
from datetime import datetime

# Name of the my assistant
name = 'Sylvanas'

voice = pyttsx3.init() # Inicializar

# Obetener la lista de voces y establecerla
get_voices = voice.getProperty('voices') # Obtener todas las voces disponibles
voice.getProperty('voice', get_voices[0].id) # Configurar la propiedad de la voz

# Configuración de voz
voice.getProperty('rate', 150)
voice.getProperty('volume', 0.8)

def talk(text):
    voice.say(text)
    voice.runAndWait()

while True:
    # Reconocer la voz
    listener = txt.Recognizer()
    # Activar micrófono
    with txt.Microphone() as src:
        print("Escuchando...")
        audio = listener.listen(src, phrase_time_limit=5)
        reco = listener.recognize_google(audio)
        print(reco)
