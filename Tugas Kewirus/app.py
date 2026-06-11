import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Mendapatkan lokasi folder file app.py saat ini
current_dir = os.path.dirname(os.path.abspath(__file__))
# Mengarahkan ke file index.html di folder yang sama
html_path = os.path.join(current_dir, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_data = f.read()

components.html(html_data, height=1000, scrolling=True)
