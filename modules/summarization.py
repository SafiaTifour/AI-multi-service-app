import streamlit as st
from huggingface_hub import InferenceClient
from utils.config import get_huggingface_api_key

def text_summarization():
    st.header("📄 Text Summarization")
    text = st.text_area("Enter text to summarize:")
    if st.button("Summarize"):
        if text:
            api_key = get_huggingface_api_key()
            client = InferenceClient(api_key=api_key)
            result = client.summarization(text=text, model="facebook/bart-large-cnn")
            st.write("Summary:", result)
