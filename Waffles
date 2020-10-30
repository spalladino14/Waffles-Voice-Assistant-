import speech_recognition as sr
from time import ctime
import subprocess, time
import pyttsx3
import os
#print(sr.Microphone.list_microphone_names())
r = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
def record():
    with sr.Microphone(device_index =2) as mic:
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
        audio_data = ''
        try:
            audio_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            engine.say('What did you say?')
            engine.runAndWait()
            engine.stop()
        except sr.RequestError:
            engine.say("I cant listen right now cause I have errors.")
            engine.runAndWait()
            engine.stop()
        return audio_data

def response(audio_data):
    if "what is your name" in audio_data:
        engine.say('My name is Waffles')
        engine.runAndWait()
        engine.stop()
    if "what time is it" in audio_data:
        engine.say(ctime())
        engine.runAndWait()
        engine.stop()
    if "I need motivation" in audio_data:
        exec(open('Final.py').read())
    if 'stop' in audio_data:
        exit()

time.sleep(1)
print('What do you want?')
while 1:
    audio_data = record()
    print(audio_data)
    response(audio_data)
