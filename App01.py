import streamlit as st
from PIL import Image 

st.title("Llama entrevistada")
st.header("No es una llama, pero suena mas divertido que un ciervo")
st.write("texto texto, mucho texto")
image = Image.open("LlamaHabla.png")

st.image(image, caption="muy seria, no sabemos de que era la entrevista")

texto = st.text_input("escribo aca algo diferente", "Demasiado diferente")
st.write("el texto escrito es: ", texto)

col1, col2 = st.columns(2) 

with col1:
  st.subheader ("Es mucho texto?")
  st.write("texto texto texto y mas texto... mucho texto")
  resp = st.checkbox("definitivamente es mucho texto")
  if resp:
    st.write("Correcto")

with col2:
  st.subheader ("Otra pregunta:")
  modo = st.radio("Cual es el animal de la imagen", ("Venado" , "Llama", "Ciervo"))
  if modo == "Venado":
    st.write("seguro?")
  if modo == "Llama":
    st.write("Tal vez si, tal vez no")
  if modo == "Ciervo":
    st.write("si tu lo dices...")






    

