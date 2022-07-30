import streamlit as st

if "button1" not in st.session_state:
    st.session_state.button1 = False

def callback():
    st.session_state.button1 = True

if (
    st.button("นำเข้าไฟล์หนังสือ", on_click = callback)
    or st.session_state.button1
):
    st.file_uploader("Upload your file here",type=['txt','docx','pdf'])

#button1 = st.sidebar.button("นำเข้าไฟล์หนังสือ")
#if button1:
#    st.sidebar.file_uploader("Upload your file here",type=['txt','docx','pdf'])

button2 = st.button("ดูไฟล์หนังสือในคลัง")
if button2:
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)
    with col1:
        st.button("ประชาธิปไตย")
    
        if "chap1" not in st.session_state:
             st.session_state.chap1 = False

        def callback():
             st.session_state.chap1 = True

        st.image("https://cdn.pixabay.com/photo/2017/03/16/07/50/statue-2148396_960_720.jpg")
   
    with col2:
        st.button("ชีทวิชานิติปรัชญา")
        st.image("https://cdn.pixabay.com/photo/2017/12/06/07/41/head-3001159_960_720.jpg")
    
    with col3:
        st.button("บ้านเล็กในป่าใหญ่")
        st.image("https://cdn.pixabay.com/photo/2013/10/09/02/27/lake-192990_960_720.jpg")

    with col4:
        st.button("กฎหมายแรงงาน")
        st.image("https://cdn.pixabay.com/photo/2016/11/08/05/15/water-buffalo-1807517_960_720.jpg")

    with col5:
        st.button("การเงิน 101")
        st.image("https://cdn.pixabay.com/photo/2015/09/15/15/53/bank-notes-941246_960_720.jpg")

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)