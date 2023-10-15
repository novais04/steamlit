#####################
# Import Libraries
#####################

import pandas as pd 
import streamlit as st 
import altair as alt 
from PIL  import Image

###################
# Page Title
###################

image = Image.open('dna-logo.jpg')
st.image(image, use_column_width=True)

st.write("""
    # DNA Nucleotide Count Web App 
    This app counts the nucleotide composition of quet DNA        
""")

# Input Text Box

st.header("Enter DNA sequence")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # skips the sequence name ( first line)
sequence= ''.join(sequence) # concatenates list to string


st.write("""
***
""")

### print the inpput DNA sequence
st.header('INPUT (DNA sequence Query)')

### DANA Nucleotide count
st.header('OUTPUT (DNA sequence Count)')
sequence
### 1. Print dictionary
st.subheader("1. Print dictionary")
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_value = list(X.values())

X 

### 2. Print text
st.subheader('2. Print text')
st.subheader("There are " + str(X['A']) + " adenine (A)")
st.subheader("There are " + str(X['T']) + " Thymine (T)")
st.subheader("There are " + str(X['G']) + " adenine (guanine)")
st.subheader("There are " + str(X['C']) + " Thynine (cytosine)")

# 3. Display DataFrame
st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'Count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'Nucleotide'})
st.write(df)

### 4. Display Bar chart using Altair 
st.subheader("4. Display Bar chart using Altair")
p = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='Count'  
)

p = p.properties(
    width=alt.Step(80)
)

st.write(p)