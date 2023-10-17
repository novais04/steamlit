import streamlit as st
import pandas as pd
import numpy as np


st.title("Draw a line chart :chart_with_upwards_trend:")
st.markdown("""
Você pode facilmente adicionar um gráfico de linhas ao seu aplicativo com **$st.line_chart()$**. 
Nós iremos gerar uma amostra aleatória usando o Numpy e então o mapearemos.
""")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']
)

st.table(chart_data.head(5))
st.line_chart(chart_data)