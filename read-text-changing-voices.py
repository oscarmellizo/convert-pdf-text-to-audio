import pyttsx3

string = "Hola a todos cambiando voces"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say(string)
   
engine.runAndWait()