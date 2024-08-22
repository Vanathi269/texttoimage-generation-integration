import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

heading_color = "#261b63"
st.markdown(f"<h1 style='text-align: center; color: {heading_color};'>Welcome to Image Generation Application</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: {heading_color};'>Will Explore the world in hand......</h3>", unsafe_allow_html=True)

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input('Enter Prompt'),
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if st.button('Generate'):
    st.image(image)