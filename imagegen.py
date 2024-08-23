import requests
import streamlit as st
import io
from PIL import Image, UnidentifiedImageError

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

heading_color = "#261b63"
st.markdown(f"<h1 style='text-align: center; color: {heading_color};'>Welcome to Image Generation Application</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: {heading_color};'>Will Explore the world in hand......</h3>", unsafe_allow_html=True)

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

if st.button('Generate'):
    prompt = st.text_input('Enter Prompt')
    if prompt:
        image_bytes = query({"inputs": prompt})
        if image_bytes:
            try:
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image)
            except UnidentifiedImageError:
                st.error("Failed to generate image. Please try again with a different prompt.")
        else:
            st.error("No image was generated. Please try again.")
    else:
        st.warning("Please enter a prompt before generating an image.")
