import pyttsx3

string = "Hola a todos"

engine = pyttsx3.init("sapi5")
engine.say(string)

engine.runAndWait()