import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Baaki — know what's left",
    page_icon="₹",
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container {padding: 0 !important; max-width: 100% !important;}
        header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "site.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=2400, scrolling=True)