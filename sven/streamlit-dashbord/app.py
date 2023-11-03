# @Email:  contact@pythonandvba.com
# @Website:  https://pythonandvba.com
# @YouTube:  https://youtube.com/c/CodingIsFun
# @Project:  Sales Dashboard w/ Streamlit


import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.figure_factory as ff 

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

colorscale = [[0, '#1d004c'],[0.5, '#7d104c'], [1, '#ffffff']]
font=['#FCFCFC', '#00EE00', '#FF3030']

st.set_page_config(
    page_title="Sales Dasboard",
    page_icon=":bar_chart:",
    layout='wide')

# add data
#st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io='supermarkt_sales.xlsx',
        engine='openpyxl',
        sheet_name='Sales',
        skiprows=3,
        usecols='B:R',
        nrows=1000
    )

    # Add hour in dataframe
    df['hour']=pd.to_datetime(df['Time'], format="%H:%M:%S").dt.hour
    df['hour'].astype(int)
    return df

df = get_data_from_excel()


# ------ SIDEBAR------
st.sidebar.header("Please Filter Here: ")
city = st.sidebar.multiselect( "Select the City: ", options=df['City'].unique(),)
#    default=df['City'].unique())
if not city:
    df2 = df.copy()
else:
    df2=df[df['City'].isin(city)]

customer_type=st.sidebar.multiselect("Select the Customer Type:", options=df['Customer_type'].unique(),)
#   default=df['Customer_type'].unique()
if not customer_type:
    df3 = df2.copy()
else:
    df3=df2[df2['Customer_type'].isin(customer_type)]

# Gender
gender=st.sidebar.multiselect("Select the Gender:", options=df['Gender'].unique(),)
 #   default=df['Gender'].unique(),

# filter the data 
if not city and not customer_type and not gender:
    filtered_df = df
elif not customer_type and not gender:
    filtered_df=df[df['City'].isin(city)]
elif not city and not gender:
    filtered_df=df[df['Customer_type'].isin(customer_type)]
elif customer_type and gender:
    filtered_df=df3[df['Customer_type'].isin(customer_type)&df3['Gender'].isin(gender)]
elif city and gender:
    filtered_df=df3[df['City'].isin(city)&df3['Gender'].isin(gender)]
elif city and customer_type:
    filtered_df=df3[df['City'].isin(city)&df3['Customer_type'].isin(customer_type)]
elif gender:
    filtered_df=df3[df['Gender'].isin(gender)]
else:
    filtered_df=df3[df['City'].isin(city)&df3['Customer_type'].isin(customer_type)&df3['Gender'].isin(gender)]



st.dataframe(filtered_df)