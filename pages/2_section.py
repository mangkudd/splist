from xmlrpc.client import TRANSPORT_ERROR
import streamlit as st
"""import keyboard

while True:
    if keyboard.is_pressed("ctrl+0")"""


st.header("สารบัญ")
st.button("บทนำ แนวทางประชาธิปไตยที่เหมาะสมในทัศนะผู้เขียน")

if "chap1" not in st.session_state:
    st.session_state.chap1 = False

def callback():
    st.session_state.chap1 = True

if (
    st.button("บทที่ 1 ประชาธิปไตยในบริบทสากล", on_click = callback)
    or st.session_state.chap1
):
    topic1_1 = st.button("1.1 ประชาธิปไตย คืออะไร")
    topic1_2 = st.button("1.2 รูปแบบการปรองระบอบประชาธิปไตย")

    if topic1_2:
        st.button("1.2.1 ประชาธิปไตยทางตรง (Direct Democracy)")
        st.button("1.2.2 ประชาธิปไตยแบบมีผู้แทน (Representative Democracy)")

#Chapter 2
if "chap2" not in st.session_state:
    st.session_state.chap2 = False

def callback():
    st.session_state.chap2 = True
    st.session_state.chap1 = False
if (
    st.button("บทที่ 2 ประชาธิปไตยในประเทศไทย", on_click = callback)
    or st.session_state.chap2
):
    topic2_1 = st.button("2.1 รูปแบบการปรองระบอบประชาธิปไตย")
    if  topic2_1:
        st.button("2.1.1 คิดว่าประชาธิปไตยคือการเลือกตั้ง")
        st.button("2.1.2 คิดว่ารัฐธรรมนูญดีจะทำให้เกิดประชาธิปไตยที่เข็มแข็ง")

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)