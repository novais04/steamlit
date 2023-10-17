# Layout
import streamlit as st


st.title("Layout")
st.markdown("""
O Streamlit torna mais fácil organizar seus widgets em uma barra lateral 
do painel esquerdo com `st.sidebar`. Cada elemento que é passado para `st.sidebar` é fixado à esquerda, permitindo que os usuários se concentrem no conteúdo do seu aplicativo enquanto ainda têm acesso aos controles da interface do usuário.

Por exemplo, se quiser adicionar um selectbox e um slider a uma barra lateral,
 use `st.sidebar.slider` e `st.sidebar.selectbox` em vez de st.slider e st.selectbox`:
""")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    "Como você gostaria de se conectado?",
    ('E-mal', 'Home Phone', 'Mobile Phone')
)

# add 0 silder to the sidebar

add_slider = st.sidebar.slider(
    "Select a range of value",
    0.0, 100.0, (250.0, 75.0 )
)