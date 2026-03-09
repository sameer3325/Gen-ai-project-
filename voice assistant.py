import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak a command...")
    audio = r.listen(source)

try:
    command = r.recognize_google(audio)
    print("Command:",command)

except:
    print("Could not understand")