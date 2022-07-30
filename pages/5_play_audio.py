import streamlit as st

    
if st.button("play"):
    audio_file = open("sample.wav", 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format = 'audio/wav')