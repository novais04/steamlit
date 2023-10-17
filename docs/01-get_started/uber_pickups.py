import streamlit as st 
import pandas as pd 
import numpy as np 

st.title('Uber pickup in NYC')

# Buscando alguns dados

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data 

# Crie um elemento de texto e deixe o leitor saber que os dados estão sendo carregados.
data_load_state = st.text('Loading data...')

# Carregar 10.000 linhas de dados no dataframe
data = load_data(10000)

# Notificar o leitor que os dados foram carregados com sucesso.
data_load_state.text('Loading data...done')
                     
