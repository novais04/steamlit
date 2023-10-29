# How to Build a Simple Machine Learning Web App in Python - Streamlit Tutorial #2
# fonte: https://www.youtube.com/watch?v=8M20LyCZDOY&t=332s
import streamlit as st 
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


st.title("Simple Iris Floower Predict 🌹")
st.markdown('''
This app predict the Iris Flower Type
''')

st.sidebar.header("Use input parameters")
def use_input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Pettal Width', 0.1, 2.5, 0.2)
    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width,
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = use_input_features()

st.subheader("Use inpuy parameters")
st.write(df)

iris = load_iris()
X = iris.data
y = iris.target

rf = RandomForestClassifier()
rf.fit(X, y)

prediction = rf.predict(df)
prediction_proba = rf.predict_proba(df)

st.subheader("class labels d their corresponding index numbers")
st.write(iris.target_names)

st.subheader("Prediction")
st.write(iris.target_names[prediction])

st.subheader("Prediciton probability")
st.write(prediction_proba)