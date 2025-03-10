import pyaudio
import pandas as pd
import wave
#from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import time


format = pyaudio.paInt16
channels = 1
rate = 16000
#record audio
p = pyaudio.PyAudio()
stream = p.open(format=format, channels=channels,rate=rate,input=True)
print('Recording...Play a Note')
while True:
    try:
        recordata = np.frombuffer(stream.read(2048), dtype=np.int16)
        recordata = recordata.astype(np.float32) / 32768.0

        D = np.abs(librosa.stft(recordata, n_fft=2048))
        frequencies, magnitudes = librosa.piptrack(S=D, sr=44100)
        index = np.argmax(magnitudes, axis=0)
        freq = np.mean(frequencies[index])
        if freq>0:
            note = librosa.hz_to_note(freq)
            print(f"Detected Note {note}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("Stopped")
        stream.stop_stream()
        stream.close()
        p.terminate()