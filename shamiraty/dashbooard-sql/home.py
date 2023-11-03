import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import sqlite3
import time

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

# Função que carrega o dataframe
def load_date():

    # Conctando banco de dados
    conn = sqlite3.connect('mydb.db')

    # dataframe
    df = pd.read_sql_query('SELECT * FROM insurance', conn)
    #desconctando banco de dados
    conn.close()

    return df

st.set_page_config(
    page_title="DashBoard",
    page_icon=":bar_chart",
    layout='wide'
)
st.subheader("🔔 Insurance Descriptive Analysis")
st.markdown("##")

# dataset
df = load_date()

theme_plotly = None # None or streamlit

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#side bar
st.sidebar.image("data/logo1.png",
                 caption="Developed and Maintaned by: samir")

# Switcher
st.sidebar.header("Please Filter")
region=st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique(),
)
location=st.sidebar.multiselect(
    'Select Location',
    options=df['Location'].unique(),
    default=df['Location'].unique(),
)
construction=st.sidebar.multiselect(
    "select Location",
    options=df['Construction'].unique(),
    default=df['Construction'].unique(),
)
df_selection =df.query(
    "Region==@region & Location==@location & Construction==@construction"
)

#with st.expander("Dataset"):
#    st.write(df_selection.style.background_gradient(cmap='Blues'))
def Home():
    with st.expander("⏰ My Excel WorkBook"):
        showData=st.multiselect(
            "Filter: ",
            options=df_selection.columns, default=["Policy","Expiry","Location","State","Region","Investment","Construction","BusinessType","Earthquake","Flood","Rating"])
        st.dataframe(df_selection[showData], use_container_width=False)

# computer top analisys
    total_investiment=float(df_selection['Investment'].sum()/1000)
    mode_investiment=float(df_selection['Investment'].mode())
    mean_investiment=float(df_selection['Investment'].mean())
    median_investiment=float(df_selection['Investment'].median())
    rating=float(df_selection['Rating'].sum())

    total1, total2, total3, total4, total5=st.columns(5 , gap='large')
    with total1:
        st.info('Total Investiment', icon='📌')
        st.metric(label="Sum TZS", value=f"$ {total_investiment:,.0f}M")

    with total2:
        st.info('Mode Frequent', icon='📌')
        st.metric(label="Mode TZS", value=f"$ {mode_investiment:,.0f}")

    with total3:
        st.info("Average Frequent", icon='📌')
        st.metric(label="Avarege TZS", value=f"$ {mean_investiment:,.0f}")

    with total4:
        st.info('Central Earings', icon='📌')
        st.metric(label="Median TZS", value=f"$ {median_investiment:,.0f}")

    with total5:
        st.info('Ratings', icon='📌')
        st.metric(label="Retings TZS", value=numerize(rating),help=f"""Total Rating: {rating}""")
st.markdown("""---""")

def graphs():
    # simple bar graph
    investment_by_business_type=(
        df_selection.groupby(by=['BusinessType']).count()[['Investment']].sort_values(by='Investment'))

    fig_investment=px.bar(
        investment_by_business_type,
        x='Investment',
        y=investment_by_business_type.index,
        orientation='h',
        title='<b>Investment by Business Type </b>',
        color_discrete_sequence=['#0083b8']*len(investment_by_business_type),
        template='plotly_white'
    )
    fig_investment.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )
    # Simple line Graph
    investment_by_state = df_selection.groupby(by=['State']).count()[['Investment']]
    fig_state=px.line(
        investment_by_state,
        x=investment_by_state.index,
        y='Investment',
        orientation='v',
        title="<b> Investiment by State</b>",
        color_discrete_sequence=['#0083b8']*len(investment_by_state),
        template="plotly_white"
    )
    fig_state.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(showgrid=False)
    )

    left,right,center = st.columns(3)
    left.plotly_chart(fig_state, use_container_width=True)
    right.plotly_chart(fig_investment, use_container_width=True)

    with center:
        fig = px.pie(
            df_selection,
            values='Rating',
            names='State',
            title='<b>Region by Ratings</b>',
        )
        fig.update_layout(
            legend_title="Regions",
            legend_y=0.9,
        )
        fig.update_traces(
            textinfo="percent+label",
            textposition='inside',
        )
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

def progressbar():
    st.markdown("""<style>.StProgress > div > div > div > div { background-image: linear-gradient(to Right, #99ff99, #FFFF00)}</style>""",unsafe_allow_html=True,)
    target=3000000000
    current=df_selection['Investment'].sum()
    percent=round((current/target*100))
    mybar=st.progress(0)

    if percent>100:
        st.subheader("Target done !")
    else:
        st.write("You have ", percent, "% ", "O f", (format(target, 'd')), "TZS")
        for percent_complete in range(percent):
            time.sleep(0.1)
            mybar.progress(percent_complete+1,text="Target Percent")

def sideBar():
    with st.sidebar:
        selected=option_menu(
        menu_title="Main Menu",
        options=["Home", "progress"],
        icons=["house","eye"],#boostrap icons (https://icons.bootcss.com/)
        menu_icon="cast",
        default_index=0
    )
    if selected=="Home":
        st.subheader(f"Page: {selected}")
        Home()
        graphs()

    if selected=="progress":
        st.subheader(f"Page: {selected}")
        progressbar()
        graphs()

sideBar()
