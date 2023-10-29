import streamlit as st

md = st.text_area("Type in your markdown string (without outer quotes)",
				  "Happy streamlit-ing! :balloon:")


st.code(f"""
import streamlit as st

st.marksown('''{md}''')
""")

st.markdown(md)