import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
import pandas as pd
import docx2txt
from PIL import Image 
from PyPDF2 import PdfFileReader
import pdfplumber


docx_file = st.file_uploader("Upload your file here",type=['txt','docx','pdf'])
if st.button("ถอดข้อความ"):
	if docx_file is not None:
		file_details = {"Filename":docx_file.name,}
		st.write(file_details)
		# Check File Type
		if docx_file.type == "text/plain":
			# raw_text = docx_file.read() # read as bytes
			# st.write(raw_text)
			# st.text(raw_text) # fails
			st.text(str(docx_file.read(),"utf-8")) # empty
			raw_text = str(docx_file.read(),"utf-8") # works with st.text and st.write,used for futher processing
			# st.text(raw_text) # Works
			st.write(raw_text) # works
		elif docx_file.type == "application/pdf":
			# raw_text = read_pdf(docx_file)
			# st.write(raw_text)
			try:
				with pdfplumber.open(docx_file) as pdf:
					page = pdf.pages[0]
					st.write(page.extract_text())
			except:
				st.write("None")
					    
					
		elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
		# Use the right file processor ( Docx,Docx2Text,etc)
			raw_text = docx2txt.process(docx_file) # Parse in the uploadFile Class directory
			st.write(raw_text)

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)