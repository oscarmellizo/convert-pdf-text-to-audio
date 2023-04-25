import pyttsx3

string = "Hola a todos guardando voz en un archivo"

engine = pyttsx3.init("sapi5")
engine.save_to_file(string, 'hola.mp3')

engine.runAndWait()