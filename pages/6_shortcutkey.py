import streamlit as st
import keyboard

while True:
    if keyboard.is_pressed("shift+a"):
       sample1=audio_file = open("sample.wav", 'rb')
       audio_bytes = audio_file.read()
       st.audio(audio_bytes, format = 'audio/wav')
       print(sample1)
       break