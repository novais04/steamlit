# fonte:

# como criar Dasboard basicos saindo Cufilink & streamlit

import streamlit as st 
import pandas as pd
import cufflinks as cf 
from plotly.offline import iplot
import plotly.graph_objects as go
import warnings 
warnings.filterwarnings('ignore')

print(f"streamlit Version: {st.__version__}")

# load dataset
from sklearn.datasets import load_wine
wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
wine_df['WineType']=[wine.target_names[t] for t in wine.target]#
#wine_df["WineType"]=wine_df["WineType"].map({'class_0': int(0), 'class_1':int(1), 'class_2':int(2) })
print(wine_df.head())

# Create Individual Charts
import plotly.express as px
#scatter Plot
st.sidebar.markdown("### Scatter Chart")
ingredients = wine_df.drop(labels=['WineType'], axis=1).columns.tolist()
x_axis = st.sidebar.selectbox("X-axis", ingredients)
y_axis = st.sidebar.selectbox("Y-axis", ingredients, index=1)

if x_axis and y_axis:
    scatter_fig =px.scatter(
    data_frame=wine_df,
    x=x_axis,
    y=y_axis,
    color='WineType',
    template='streamlit'
    )
    scatter_fig.update_layout(
        title= f"<b>{x_axis.replace('_', ' ').capitalize()} vs {y_axis.replace('_', ' ').capitalize()}</b>",
        xaxis_title=x_axis.replace('_', ' ').capitalize(),
        yaxis_title=y_axis.replace('_', ' ').capitalize(),
    )

# Bar chart
st.sidebar.markdown("### Bar Chart")
avg_wine_df = wine_df.groupby(by=['WineType']).mean()

bar_axis = st.sidebar.multiselect(
    "Bar char Ingredients",
    options=ingredients,
    default=['alcohol', 'malic_acid'],
)

if bar_axis:
    bar_fig=px.bar(
        avg_wine_df,
        x=avg_wine_df.index,
        y=bar_axis,
    ) 
    bar_fig.update_layout(
        title = "Distribuição Média de Ingredientes por tipo"
    )     
        
    

container1 = st.container()
col1, col2 = st.columns(2)
with container1:
    with col1:
        st.plotly_chart(scatter_fig, width=300)
    with col2:
        st.plotly_chart(bar_fig, use_container_width=True)


    

