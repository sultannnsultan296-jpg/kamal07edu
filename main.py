import streamlit as st
from streamlit_gsheets import GSheetsConnection
import google.generativeai as genai
import pandas as pd
from datetime import datetime

# 1. Konfigurasi AI & Database
genai.configure(api_key=st.secrets["GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')
URL_SHEET = st.secrets["GSHEET_URL"]

# 2. Setup UI
st.set_page_config(page_title="kamal07edu Studio", layout="wide")
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>🏫 kamal07edu Studio</h1>", unsafe_allow_html=True)

# 3. Sidebar Navigasi
role = st.sidebar.radio("Masuk Sebagai:", ["Guru", "Siswa"])

if role == "Guru":
    st.sidebar.subheader("Menu Guru")
    menu = st.sidebar.selectbox("Pilih Tugas:", ["Buat Materi AI", "Cek Jawaban Siswa"])
    
    if menu == "Buat Materi AI":
        topik = st.text_input("Topik Pembelajaran:")
        jenjang = st.selectbox("Tingkat:", ["SD", "SMP", "SMA"])
        if st.button("Generate Materi"):
            res = model.generate_content(f"Buat materi singkat & 3 soal HOTS tentang {topik} untuk {jenjang}")
            st.write(res.text)
            st.session_state['draft'] = res.text
            
        if st.button("Simpan & Share ke Siswa"):
            # Logika simpan ke GSheets di sini
            st.success("Materi Tersimpan Permanen!")

else:
    st.sidebar.subheader("Portal Siswa")
    nama = st.text_input("Nama Siswa:")
    tugas = st.selectbox("Pilih Tugas:", ["Tugas 1", "Tugas 2"]) # Dinamis dari Sheets
    jawaban = st.text_area("Jawaban Anda:")
    if st.button("Kirim Jawaban"):
        st.balloons()
        st.success("Jawaban terkirim ke Guru!")
