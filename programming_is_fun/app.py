import streamlit as st
import plotly.express as px 
import pandas as pd
import os 
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="SuperStore!!!",
    page_icon=":bar_chart:",
    layout='wide'
)

st.title(":bar_chart: Sample SuperStore EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

# UPLOAD DATA
f1 = st.file_uploader(":file_folder: Upload a file", type=(['csv','txt', 'xlsx', 'xls']))
if f1 is not None:
    filename = f1.name 
    st.write(filename)
    df = pd.read_csv(filename,  encoding="ISO-8859-1")
else:
    os.chdir('/Users/anselmo/Documents/dev/python/Dash_plotly/streamlit/programming_is_fun')
    df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")

col1, col2 = st.columns((2))
df['Order Date']=pd.to_datetime(df['Order Date'])

# getting the min and max date
startDate = pd.to_datetime(df['Order Date']).min()
endDade = pd.to_datetime(df['Order Date']).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDade))
    
df = df[(df['Order Date']>=date1) & (df['Order Date']<=date2)].copy()

st.sidebar.header("Chose you rFilter: ")
# regiam
region = st.sidebar.multiselect("Pick your region", df['Region'].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

# state
state = st.sidebar.multiselect("Pick tge state: ", df2['State'].unique())
if not state:
    df3 = df2.copy()
else:
    df3=df2[df2['State'].isin(state)]
    
# City
city = st.sidebar.multiselect("Pick the city", df3['City'].unique())


# Filter the data based on Region, state and city
if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df['Region'].isin(region)]
elif not region and not city:
    filtered_df = df[df['State'].isin(state)]
elif state and city:
    filtered_df = df3[df['State'].isin(state) & df3['City'].isin(city)]
elif region and city:
    filtered_df = df3[df['Region'].isin(region) & df3['City'].isin(city)]
elif region and state:
    filtered_df = df3[df['Region'].isin(region) & df3['State'].isin(state)]
elif city:
    filtered_df=df3[df3['City'].isin(city)]
else:
    filtered_df = df3[df3['Region'].isin(region)&df3['State'].isin(state)&df3['City'].isin(city)]

category_df = filtered_df.groupby(by=["Category"], as_index=False)['Sales'].sum()

with col1:
    st.subheader("Category wise Sales")
    fig_category = px.bar(
        category_df,
        x='Category',
        y='Sales',
        text=["${:,.2f}".format(x) for x in category_df['Sales']],
        template="plotly_white"    )
    st.plotly_chart(fig_category, use_container_width=True, height=200)
with col2:
    st.subheader("Region wise Sales")
    fig_region = px.pie(filtered_df,values = "Sales", names="Region", hole=0.5)
    fig_region.update_traces(text=filtered_df["Region"], textposition="outside")
    st.plotly_chart(fig_region, use_container_width=True)

col1, col2 = st.columns((2))
with col1:
    with st.expander("Category_ViewData"):
        st.write(category_df.style.background_gradient(cmap="Blues"))
        csv = category_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Data", data = csv, file_name="Category_csv", mime = "text/csv",
                           help = "Click here to download the data as a CSV file")
        
    with col2:
        with st.expander("region_ViewData"):
            region = filtered_df.groupby(by = "Region", as_index = False)["Sales"].sum()
      #     st.write(region.style.background_gradient(cmap="Oranges"))
            st.write(region.style.background_gradient(cmap="Oranges"))
            csv = region.to_csv(index=False).encode("utf-8")
            st.download_button("Download Data", data = csv, file_name="Region_csv", mime = "text/csv",
                            help = "Click here to download the data as a CSV file")
filtered_df['month_year']=filtered_df['Order Date'].dt.to_period('M')
st.subheader("Time Series Analysys")

linechart=pd.DataFrame(filtered_df.groupby(filtered_df['month_year'].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()

fig2 = px.line(
    data_frame=linechart,
    x='month_year',
    y='Sales',
    labels={'Sales': 'Amount'},
    height=500,
    width=1000,
    template='gridon'
    )
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Data of TimeSeries"):
    st.write(linechart.T.style.background_gradient(cmap='Blues'))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button("Download Data", data = csv, file_name="TimeSeries.csv", mime='text/csv')

# Create a treem based on Region, category, sub-category
st.subheader("Hierichal view of sales usung TreeMap")
fig3 = px.treemap(
    data_frame=filtered_df,
    path=['Region', 'Category', 'Sub-Category'],
    values='Sales',
    hover_data=['Sales'],
    color='Sub-Category',
)

fig3.update_layout(
    width=800,
    height=650
)

st.plotly_chart(fig3, use_container_width=True)


chart1, chart2 = st.columns((2))
with chart1:
    st.subheader("Segment wide Sales")
    fig = px.pie(filtered_df, values='Sales', names='Segment', template='plotly_dark')
    fig.update_traces(text=filtered_df['Segment'], textposition='inside')
    st.plotly_chart(fig, use_container_width=True)
    
with chart2:
    st.subheader("Category wide Sales")
    fig = px.pie(filtered_df, values='Sales', names='Category', template='plotly_dark')
    fig.update_traces(text=filtered_df['Category'], textposition='inside')
    st.plotly_chart(fig, use_container_width=True)
    
import plotly.figure_factory as ff 
st.subheader(":point_right: Month wise Sub-Category Sales Summary")
with st.expander("Sumary_table"):
    df_sample = df[0:5][['Region', 'City','Category', 'Sales', 'Profit', 'Quantity']]
    fig = ff.create_table(
        df_sample,
        colorscale='Cividis',        
    )    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("Month wise Sub-Category Table")
    filtered_df['month'] = filtered_df['Order Date'].dt.month_name()
    sub_category_year=pd.pivot_table(
        data=filtered_df,
        values='Sales',
        columns='month',
        index=['Sub-Category']
    )
    st.write(sub_category_year.style.background_gradient(cmap='Blues'))
    
# Create scater plot 
data1 = px.scatter(
    data_frame=filtered_df,
    x='Sales',
    y='Profit',
    size='Quantity'
)
data1.update_layout(
    title ="<b>Relationship Between Sales and Profis using Scatter Plot</b>",
    titlefont=dict(size=20),
    xaxis=dict(title='Sales',titlefont=dict(size=19)),
    yaxis=dict(title='Profit',titlefont=dict(size=19)),
)
st.plotly_chart(data1, use_container_with=True)


with st.expander("View Data"):
    st.write(filtered_df.iloc[:500,1:20:2].style.background_gradient(cmap='Oranges'))
    
# dowaload orginal dataset
csv = df.to_csv(index=False).encode('utf8')
st.download_button("Download Data", data = csv, file_name=r"../programming_is_fun/dataData.csv", mime="text/csv")
