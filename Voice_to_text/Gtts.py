import gtts
from gtts import gTTS
from playsound import playsound


# tts = gtts.gTTS("Hello world")
print("Type something:")
sen = input()
audio = gtts.gTTS(sen)
audio.save("C:/Users/Jayanth B R/Desktop/Chaithra/Voice_to_text/audio.mp3")
playsound("audio.mp3")

