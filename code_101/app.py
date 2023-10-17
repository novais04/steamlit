# Streamlit tutorial - The fastest way to build web apps in python [2022-23]
import streamlit as st 
import pandas as pd 
from PIL import Image

# title
st.title("Streamlit begginer's Guide")

# Headers
st.header("This is the heading")

# Subheaders
st.subheader("This is the subheading")

# text
st.text("Olá, Bem-vindo ao AiranCode")

# Success info
st.success("Excuted Successfully")
st.info("Esta é uma infomação")
st.warning("Este é um alert")
st.error("Este uma msg de erro")

#write
st.write("Eu escrevo um códio simples")
st.write(range(20))

channel = "eiranCodecomAnselmo"
st.write("Assine meu canal ", channel)

# Code
code_body = '''
    for in in range(10):
        print(i)
'''
st.code(code_body,language='python')

if(st.checkbox("Eu concordo")):
    st.write("Você concordou com as condições")

val = st.radio("Escolha a lingagem", ('pyhton','java', 'C'))

st.write(f"{val} was selected")

# Image
img = Image.open("streamlit_logo.jpeg")
st.image(img)

# Selection box / dropdown
option = st.selectbox(
    "Select an option: ",
    ['python', 'Javas', 'react', 'node', 'sql']
)
st.write(f"Você escolheu {option} ")

# Multple select
options = st.multiselect(
    "Select multiple options",
    ['python', 'Javas', 'react', 'node',]
)
st.write ("Você escolhe: ")
for each_op in options:
    st.write(each_op)
    
# text input box
name = st.text_input("Entre com o seu nome: ")
st.write(f"Seu nome é : {name}")

# button
st.button("Click me!")
if(st.button("SubScribe")):
    st.text("Obrigado por assinar o canal EiraCode!")

# Slider
sal = st.slider("Your salary is ", 10000, 50000)
st.write(f"Seu salário é {sal}")