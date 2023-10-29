# example-001.py

# Comandos mágicos são um recurso no Streamlit que permite escrever quase tudo (markdown, dados, gráficos) 
# sem ter que digitar um comando explícito. Basta colocar a coisa que deseja mostrar na sua própria linha de código, 
# e ela irá aparecer na sua aplicação. Aqui está um exemplo:

# Draw a title and some text to the app:
import streamlit as st 


'Hello, world'

'''
# This is the document title

This is some _markdown_.
'''
import pandas as pd 
df = pd.DataFrame(
    {
        'col1': [1, 2, 3],
        'col2': [4, 5, 6],
    }
)
df

x = 10
'x', x

import numpy as np
import matplotlib.pyplot as plt

y = np.random.normal(0,1,size=1000)
fig, ax = plt.subplots()
ax.hist(y, bins=20)

fig