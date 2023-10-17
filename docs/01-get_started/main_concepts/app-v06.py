# Widgets
import streamlit as st

x = st.slider('x')

st.write(x, "square is", x * x)