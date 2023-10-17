import streamlit as st

st.write("""
## Example using code()
""")

code = '''
def hello():
	print("Hello, Streamlit!")
'''
st.code(code, language='python')
