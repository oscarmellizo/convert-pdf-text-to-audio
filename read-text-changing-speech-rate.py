import pyttsx3

string = "Hola a todos cambiando nivel de conversacion"

engine = pyttsx3.init("sapi5")
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 50)
engine.say(string)
engine.runAndWait()