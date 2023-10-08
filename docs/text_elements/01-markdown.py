import streamlit as st

st.markdown("__Streamlist__ is **really** ***cool***.")
st.markdown('''
	:red[Stramlit] :orange[can] :green[write] :blue[text] :violet[in]
	:gray[pretty] :rainbow[colors].''')

st.markdown("Here's a bouquet &mdash;\
	:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return for the next line.

Two (or more) newline characters in a row will resutl in a hard return.
'''

st.write(multi)