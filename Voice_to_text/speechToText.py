# !pip install SpeechRecognition
import speech_recognition as sr
# r = sr.Recognizer()
# sr.Microphone.list_microphone_names()
# mic = sr.Microphone(device_index=1)
# with mic as source:
#     audio = r.listen(source)
#     r.recognize_google(audio)
#     r.recognize_google(audio, language="fr-FR")

def speech():
    ear = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("listening...")
        audio = ear.listen(sourse)
        try:
            text = ear.recognize_google(audio)
            print(text)
        except:
            print("i didn't get that...")
speech()



# import audiomath; audiomath.RequireAudiomathVersion( '1.12.0' )
# import speechrecognition  # NB: python -m pip install SpeechRecognition

# class DuckTypedMicrophone( speech_recognition.AudioSource ): # descent from AudioSource is required purely to pass an assertion in Recognizer.listen()
#     def __init__( self, device=None, chunkSeconds=1024/44100.0 ):  # 1024 samples at 44100 Hz is about 23 ms
#         self.recorder = None
#         self.device = device
#         self.chunkSeconds = chunkSeconds
#     def __enter__( self ):
#         self.nSamplesRead = 0
#         self.recorder = audiomath.Recorder( audiomath.Sound( 5, nChannels=1 ), loop=True, device=self.device )
#         # Attributes required by Recognizer.listen():
#         self.CHUNK = audiomath.SecondsToSamples( self.chunkSeconds, self.recorder.fs, int )
#         self.SAMPLE_RATE = int( self.recorder.fs )
#         self.SAMPLE_WIDTH = self.recorder.sound.nbytes
#         return self
#     def __exit__( self, *blx ):
#         self.recorder.Stop()
#         self.recorder = None
#     def read( self, nSamples ):
#         sampleArray = self.recorder.ReadSamples( self.nSamplesRead, nSamples )
#         self.nSamplesRead += nSamples
#         return self.recorder.sound.dat2str( sampleArray )
#     @property
#     def stream( self ): # attribute must be present to pass an assertion in Recognizer.listen(), and its value must have a .read() method
#         return self if self.recorder else None

# if __name__ == '__main__':
#     import speech_recognition as sr
#     r = sr.Recognizer()
#     with DuckTypedMicrophone() as source:
#         print('\nSay something to the %s...' % source.__class__.__name__)
#         audio = r.listen(source)
#     print('Got it.')
#     print('\nUnderstood: "%s"\n' % r.recognize_google(audio))

#     if 0: # plot and/or play back captured audio
#         s = audiomath.Sound(audio.get_wav_data(), fs=audio.sample_rate, nChannels=1)
#         s.Play()
#         s.Plot()