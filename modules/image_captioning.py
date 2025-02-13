import streamlit as st
import requests
from utils.config import get_huggingface_api_key

def image_captioning():
    st.header("🖼️ Image Captioning")
    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        if st.button("Generate Caption"):
            api_key = get_huggingface_api_key()
            url = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
            headers = {"Authorization": f"Bearer {api_key}"}
            image_bytes = uploaded_file.read()
            response = requests.post(url, headers=headers, data=image_bytes)
            caption = response.json()
            st.write("Generated Caption:", caption[0]["generated_text"])
