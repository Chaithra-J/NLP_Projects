#!pip install SpeechRecognition
import speech_recognition as sr
r = sr.Recognizer()
sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=1)
with mic as source:
    audio = r.listen(source)
    r.recognize_google(audio)
    r.recognize_google(audio, language="fr-FR")
