import pyaudio
import speech_recognition
import json


recognizer = speech_recognition.Recognizer()
stop_words = input("Enter stop phrase here:").lower()
textstring = ''
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            audioinput = recognizer.listen(mic)
            text = recognizer.recognize_google(audioinput)
            print(f"{text}"+".")
            textstring += f"{text}"+"."+ " "
            if stop_words+'.' in textstring:
                print('Done.')
                textstring = textstring.replace(stop_words+".", '')
                print(textstring)
                break
    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        continue
todict = {"text":textstring}
filepath = "output.jason"
with open(filepath, 'w') as json_file:
    json.dump(todict, json_file, indent=4)