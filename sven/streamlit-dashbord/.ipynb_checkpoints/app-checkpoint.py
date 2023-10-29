# @Email:  contact@pythonandvba.com
# @Website:  https://pythonandvba.com
# @YouTube:  https://youtube.com/c/CodingIsFun
# @Project:  Sales Dashboard w/ Streamlit


import pandas as pd
import plotly.express as px
import streamlit as st


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="Sales Dasboard",
    page_icon=":bar_chart:",
    layout='wide')


df = pd.read_excel(
    io='supermarkt_sales.xlsx',
    engine='openpyxl',
    sheet_name='Sales',
    skiprows=3,
    usecols='B:R',
    nrows=1000
)

#st.dataframe(df)

# ------ SIDEBAR------
st.sidebar.header("Please Filter Here: ")
city = st.sidebar.multiselect(
    "Select the City: ",
    options=df['City'].unique(),
    default=df['City'].unique()
)

customer_type=st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df['Customer_type'].unique(),
    default=df['Customer_type'].unique()
)

gender=st.sidebar.multiselect(
    "Select the Gender:",
    options=df['Gender'].unique(),
    default=df['Gender'].unique(),
)

df_selection=df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)

st.dataframe(df_selection)

# ---- MAINPAGE -----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# ---- TOP KIP'S ----
total_sales=int(df_selection['Total'].sum())
average_rating=round(df_selection['Rating'].mean(),1)
star_rating=":star:"* int(round(average_rating,0))
average_sale_by_transaction=round(df_selection['Total'].mean(),2)

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
    
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")

with right_column:
    st.subheader("Averehe Sales per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")