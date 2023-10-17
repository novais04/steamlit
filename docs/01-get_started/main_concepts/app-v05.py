

import streamlit as st
import pandas as pd
import numpy as np


st.title("Plot a map :bar_chart:")
st.markdown("""
Com `st.map()` poderá mostrar os pontos de dados num mapa. Vamos usar o Numpy para 
gerar alguns dados de exemplo e para os representar num mapa de São Francisco.
""")

map_data = pd.DataFrame(

    np.random.randn(1000,2 )/ [50, 50] + [37.76, -112.4],
    columns=['lat', 'lon']

)
st.map(map_data)