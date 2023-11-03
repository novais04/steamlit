import streamlit as st 
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

st.set_page_config(
    page_title="NBA Player Stats Explorer",
    page_icon="🏀")

st.title("NBA Player Stats Explorer")


st.markdown("""
This app performs simple webscraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

st.sidebar.header('Use Input Features')
selected_year = st.sidebar.selectbox(
    'Year',
    options=list(range(1950,2020)),
)

# web scraping of NBA player stats
@st.cache 
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html=pd.read_html(url, header=0)
    df=html[0]
    raw=df.drop(df[df.Age=='Age'].index)
    raw=raw.fillna(0)
    playerstats=raw.drop(['Rk'],axis=1)
    return playerstats
    
playerstats= load_data(selected_year)

# Sidebar - team selction
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect(
    'Team',
    sorted_unique_team,
    default=sorted_unique_team
)

#sidebar - position selection
unique_pos=['C','PF', 'SF', 'PG','SG']
selected_pos=st.sidebar.multiselect(
    'Position',
    options=unique_pos,
    default=unique_pos
)

# filtering data
df_selcted_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header("Dispaly Player Stats of Selected Team(s)")
st.write("Data Dimension: "+ str(df_selcted_team.shape[0]) +
         " rows and " + str(df_selcted_team.shape[1]))
st.dataframe(df_selcted_team, height=320)

# Downlad dataset

csv = df_selcted_team.to_csv(index=False).encode('utf8')
st.download_button(
    'Download Data',
    data=csv,
    file_name='output.csv',
    mime='text/csv'
)

#heatmap
if st.button("Inercorelação heatmao"):
    st.header("Intercorrelação Matrix Heatmap")
    df_selcted_team.to_csv('output.csv', index=False)
    df=pd.read_csv('output.csv')
    df=df.drop(['Player','Pos','Tm'], axis=1)
    corr=df.corr()
    mask=np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style('white'):
        fig, ax = plt.subplots(figsize=(7,5))
        ax=sns.heatmap(corr, mask=mask, vmax=1 , square=True)
        fig
    




    