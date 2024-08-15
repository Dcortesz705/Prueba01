import streamlit as st
from PIL import Image 

st.title("Llama entrevistada")
st.header("No es una llama, pero suena mas divertido que un ciervo")
st.write("texto texto, mucho texto")
image = Image.open("LlamaHabla.png")

st.image(image, caption="muy seria, no sabemos de que era la entrevista")

texto = st.text_imput("escribo aca algo diferente", "Demasiado diferente")
st.write("el texto escrito es: ", texto)
