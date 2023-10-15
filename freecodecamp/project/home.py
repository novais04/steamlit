import streamlit as st 
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize

st.set_page_config(page_title="Dashbord", page_icon="🌍", layout='wide')
st.subheader("🔔 Insurance description Analyticis")