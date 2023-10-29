# example-003.py
# Passando multiplos arquimentos

import streamlit as st 
import pandas as pd

data_frame = pd.DataFrame(
    {
        'fisrt_column' : [1, 2, 3 ,4 ],
        'secund_column': [10,20,30,40],
    }
)

st.write("1 + 1 = ", 2)
st.write("Abaixo um DataFrame", data_frame, "Acima um DataFrame")