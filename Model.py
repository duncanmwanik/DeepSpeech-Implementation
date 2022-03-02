import deepspeech
import wave
import numpy as np
import os
import speech_recognition as sr

def predict_audio_deepspeech(file):
    model = deepspeech.Model('deepspeech-0.9.3-models.pbmm')
    model.enableExternalScorer('deepspeech-0.9.3-models.scorer')

    lm_alpha = 0.75
    lm_beta = 1.85
    model.setScorerAlphaBeta(lm_alpha, lm_beta)

    beam_width = 500
    model.setBeamWidth(beam_width)

    filename = 'Words/' + file
    w = wave.open(filename, 'r')
    rate = w.getframerate()
    frames = w.getnframes()
    buffer = w.readframes(frames)
    print('rate: ' + str(rate))
    print('sampleRate: ' + str(model.sampleRate()))
    type(buffer)

    data16 = np.frombuffer(buffer, dtype=np.int16)
    text = model.stt(data16)
    print(text)


def get_speech_from_text(file):

    filename = 'C:/Users/Mo/Documents/SPEECH/AUDIO/' + file
    r = sr.Recognizer()
    h = sr.AudioFile(filename)
    with h as source:
        audio = r.listen(source)
    try:
        text = predict_audio_deepspeech(audio)
        return text

    except:
        return 'Nerd'

def get_text_from_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text + '\n----------------\n')
    except:
        return 'Bla Bla noted down...'

def home():
    pred = 0
    count = 0
    for i in os.listdir('C:/Users/Mo/Documents/SPEECH/AUDIO'):
        stt = get_speech_from_text(i)
        print(stt)
        pred = pred + 1
        print(str(pred) + '\n')
        if stt == 'Nerd':
            count = count + 1
            print(str(count) + ' / ' + str(len(os.listdir('C:/Users/Mo/Documents/SPEECH/AUDIO'))))


#predict_audio('h_4')
while True:
    get_text_from_speech()