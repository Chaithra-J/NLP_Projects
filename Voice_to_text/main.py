from flask import Flask, render_template, request, jsonify, send_file
import webbrowser
import gtts
from gtts import gTTS
from playsound import playsound
import logging
# import Gtts_flask

app = Flask(__name__)
# app.config['AUDIO FOLDER'] = True

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/')
def speech():
    if request.method == 'POST':
        sen = request.form('fsen')
        print(sen)
        # audio = gtts.gTTS(sen)
        # audio.save("C:/Users/Jayanth B R/Desktop/Chaithra/Voice_to_text/audio.mp3")
        # audio_response = "audio.mp3"
        logging.info('Success')
        return render_template("main.html")
        # return send_file(audio_response)
        

    # else:
    #     return render_template("main.html")

    # result = speech
    # return render_template('main.html', inputForm = sen)




if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True, threaded=True,port=5000)
    app.run()
