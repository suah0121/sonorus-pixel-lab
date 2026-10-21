import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="소노루스 (SONORUS) 픽셀 실험실",
    page_icon="🧪",
    layout="wide"
)

# index.html 불러오기
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Streamlit 화면에 픽셀 게임 렌더링
components.html(html_code, height=850, scrolling=True)
