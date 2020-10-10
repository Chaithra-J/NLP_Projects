from flask import Flask, render_template, request, jsonify
import webbrowser
import gtts
from gtts import gTTS
from playsound import playsound


def speech():
    sen = input()
    audio = gtts.gTTS(sen)
    audio.save("./audio.mp3")
    speech = playsound("audio.mp3")
    return speech
