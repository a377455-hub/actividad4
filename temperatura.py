import streamlit as st 

st.title ("Clasificador de temperatura")

temperatura = st.number_input(20)
"Introduce la temperatura en °C"
if temperatura < 10:
 st.write("Hace frío.")
elif temperatura >10 and temperatura <=24:
 st.write("La temperatura es agradable.")
else:
 st.write("Hace calor.")
  
