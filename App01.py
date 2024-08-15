import streamlit as st
from PIL import Image 

st.title("Llama entrevistada")
st.header("No es una llama, pero suena mas divertido que un venado")
st.write("texto texto, mucho texto")
image = Image.open("LlamaHabla.png")

st.image(image, caption="muy seria, no sabemos de que era la entrevista")

