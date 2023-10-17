import streamlit as st 
import pandas as pd
import pandas_bokeh
from sklearn.datasets import load_wine

@st.cache_data
def load_data():
    wine = load_wine()
    wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
    wine_df['WineType']=[wine.target_names[t] for t in wine.target]
    return wine_df
    
wine_df = load_data()
ingredients = wine_df.drop('WineType', axis=1)

avg_wine_df = wine_df.groupby("WineType").mean().reset_index()
print(ingredients.shape)
print(avg_wine_df)

# titulo do dashboard
st.title("Wine Dataset :green[Analysis]")



