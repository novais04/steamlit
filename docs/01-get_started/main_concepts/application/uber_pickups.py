# Create your first app
import streamlit as st 
import pandas as pd
import numpy as np

# Titile
st.title("Uber pickups in NYC 🚘")

# Fetch some data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Crie um elemento de texto e deixa o user saber que os dados estão sendo carregados.
data_load_state = st.info("Loading data...")

# loading 10.000 linhas
data = load_data(10000)

# Notifica o user que os dados foram carregados com sucesso.
data_load_state = st.success("done!..using st.cahe_data")

# motrando os dados
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Draw a histogram
st.subheader("Númeors de pickups por hora")

# Use o NumPy para gerar um histograma que divide os tempos de recolha por hora:
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Vamos redesenhar o mapa para mostrar a concentração de captadores às 17:00.
hour_to_filter = st.slider('Hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f"Map of all pickups at {hour_to_filter}:00")
st.map(filtered_data)


