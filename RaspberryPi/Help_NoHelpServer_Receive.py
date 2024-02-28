import socket
import speech_recognition as sr
from os import path
import wave
import struct
import time 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
from flask import Flask, request, jsonify
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
receive_data = {}
duration = 10
start_time=None

AUDIO_FILE = "output.wav"
        
with open("model.pkl","rb") as f:
	model=pickle.load(f)

with open("vect.pkl","rb") as f:
	vect=pickle.load(f)

def receive_data(port, output_file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()
        print(f"Listening on port {port}...")

        conn, addr = s.accept()
        print(f"Connection from {addr}")

        with open(output_file, 'wb') as file:
            start_time = time.time()
            while True:
                data = conn.recv(1024)
                #if not data:
                    #break
                file.write(data)
                if time.time() - start_time >= duration:
                    break
        

            print("Data received and saved to", output_file)
        
def pcmtowav(output_file):
    with open(output_file ,'rb') as file:
        pcm_data = file.read()
        
    with wave.open("output.wav", 'w') as wav_file:
        wav_file.setnchannels(2)  # 1 channel for mono, 2 channels for stereo
        wav_file.setsampwidth(2)  # 16-bit PCMconst char* ssid     = "Galaxy";
        wav_file.setframerate(16000)  # Adjust based on your desired sample rate
        wav_file.writeframes(pcm_data)
    
    print(f"WAV file output.wav created successfully.")

def SpeechtoText(AUDIO_FILE):
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file 
        text=r.recognize_google(audio)
        print("Transcription: " + text)
    return text
        
@app.route('/', methods=['GET'])
def get_data():
    global received_data
    return jsonify(received_data)


def main():
    port_number = 8000  # Replace with your actual port number
    output_filename = "output.pcm"

    receive_data(port_number, output_filename)
    pcmtowav(output_file="output.pcm")
    try:
        text=SpeechtoText(AUDIO_FILE = "output.wav")
        sent=vect.transform([text])
        a=model.predict(sent)
        if a[0]:
            print("prediction: Help is needed")
        else:
            print("prediction: no help is needed")
        received_data = {"help":a[0]}
        app.run(host='your ip', port=1885)
    finally:
        main()                                                     

if __name__ =="__main__":
    main()
    




    
