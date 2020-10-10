import turtle
import nltk
import speech_recognition as sr

window = turtle.Screen()
r = sr.Recognizer()
geoff = turtle.Turtle()
with sr.Microphone() as source:
    print("Read the following paragraph:")
    print('I woke up early morning and got ready for school. I ate my breakfast and got down the stairs to reach the gate. I took a left from my house and walked. Then, took a right to reach my school.')
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        words = nltk.word_tokenize(text)
        print(words)
        length = int(len(words))
        print(length)
        i=1
        for i in range(length):
            print(i)
            geoff.forward(i*10)
            geoff.right(144)
       
    except:
        print("Google couldn't recognize your speech")

window.exitonclick()