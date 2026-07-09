import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter Text")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Japanese": "ja",
    "French": "fr",
    "German": "de"
}

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    translated = GoogleTranslator(
        source=languages[source],
        target=languages[target]
    ).translate(text)

    st.success(translated)
