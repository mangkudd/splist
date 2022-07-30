import streamlit as st
import streamlit_book as stb
from PIL import Image, ImageEnhance

# Set wide display
st.set_page_config(layout="wide", page_icon="https://cdn-icons-png.flaticon.com/512/607/607554.png", page_title="Splist")

# Set multipage
stb.set_chapter_config(path="pages")

button1 = st.sidebar.button("Log in")
if button1:
    with st.sidebar.form(key='my_form'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Log in')

button2 = st.sidebar.button("Sign up")
if button2:
    with st.sidebar.form(key='my_form'):
        name = st.text_input('ชื่อ-สกุล')
        username = st.text_input('ชื่อผู้ใช้')
        email = st.text_input('อีเมล')
        password = st.text_input('รหัสผ่าน')
        confirmpassword = st.text_input('ยืนยันรหัสผ่าน')
        st.form_submit_button('sign up')

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)