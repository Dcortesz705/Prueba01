import streamlit as st
from PIL import Image 

st.title("Titulo")
st.header("Subtitulo")
st.write("texto texto, mucho texto")
image = Image.open(LlamaHabla.png)

st.image(image, caption="Interfaces multimodales")

