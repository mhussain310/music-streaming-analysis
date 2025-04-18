import streamlit as st
from utils.file_utils import get_absolute_path


def load_css(file_path):
    absolute_file_path = get_absolute_path(file_path)
    with open(absolute_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
