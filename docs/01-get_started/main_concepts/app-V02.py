import streamlit as st
import pandas as pd
import numpy as np


st.markdown("""
 # Escrever um quadro de dados
Junto com `magic commands`, `st.write()` é o "canivete suíço" do Streamlit. 
Você pode passar quase qualquer coisa para `st.write()` - 
texto, dados, figuras Matplotlib,gráficos Altair e muito mais. Não se preocupe, o Streamlitvai descobrir e renderizar as coisas da maneira certa.
""")

st.write("Aqui esta nossa primeiro attempt usando dados para crear uma tabela:")
'''
st.write(
    pd.DataFrame(
        {
            'first column':[1, 2, 3, 4],
            'second column':[10, 20, 30, 40],
        }
    )
)
'''

dataFrame = np.random.randn(10,20)
st.dataframe(dataFrame)