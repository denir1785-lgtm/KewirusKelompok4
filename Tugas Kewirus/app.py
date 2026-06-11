import streamlit as st
import streamlit.components.v1 as components

# Mengatur konfigurasi halaman agar terlihat penuh
st.set_page_config(layout="wide")

# Membaca file HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Menampilkan HTML di Streamlit
# height bisa disesuaikan dengan kebutuhan (misal: 1000)
components.html(html_data, height=1000, scrolling=True)