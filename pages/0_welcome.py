import streamlit as st

st.header("ยินดีต้อนรับสู่ Splist!")
st.markdown("Splist เป็นผู้ช่วยที่จะทำให้คุณอ่านไฟล์หนังสือได้สะดวกขึ้น")
st.caption("หากคุณเป็นผู้เริ่มต้นใช้งานครั้งแรก กดคีย์ลัด *Insert + 1* เพื่อเรียนรู้คีย์ลัดและฟีเจอร์ของเรา หรือกด *Enter* เพื่อไปสู่หน้าหลัก")

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)