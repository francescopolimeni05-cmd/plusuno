from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PlusUno", page_icon="🤝", layout="wide")

HERE = Path(__file__).parent / "pages_html"


def show(file_name: str, height: int) -> None:
    html = (HERE / file_name).read_text(encoding="utf-8")
    components.html(html, height=height, scrolling=True)


st.markdown(
    "<h1 style='margin-bottom:0'>PlusUno</h1>"
    "<p style='margin-top:4px;color:#5B6B73'>Find something to do. Find someone to do it with. "
    "Connect in real life. · Design Sprint, ESADE</p>",
    unsafe_allow_html=True,
)

tab_app, tab_comic = st.tabs(["Prototipo", "Come ci siamo arrivati"])
with tab_app:
    show("prototipo.html", height=980)
with tab_comic:
    show("fumetto.html", height=2300)
