# Use selectboxes for options
import streamlit as st
import pandas as pd

df = pd.DataFrame(
    {
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }
)
#print(df)

option = st.selectbox(
    "Qual número você gosta mais?",
    df["first column"]
)
"You select: ", option