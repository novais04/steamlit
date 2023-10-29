# example001.py
import streamlit as st 
import pandas as pd 
import numpy as np

st.title("DataFrame - Exemple-001")
df = pd.DataFrame(np.random.randn(50,20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)