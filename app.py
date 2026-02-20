import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.title("Stock Market Financial Dashboard")

stocks = ["AAPL", "TSLA", "MSFT"]
selected_stock = st.selectbox("Select Stock", stocks)

data = yf.download(selected_stock, start="2020-01-01", end="2024-01-01")
data.columns = data.columns.get_level_values(0)

st.subheader("Raw Data")
st.write(data)

fig = px.line(data, x=data.index, y="Close", title="Stock Price Over Time")
st.plotly_chart(fig)

st.subheader("Volume")
fig2 = px.bar(data, x=data.index, y="Volume")
st.plotly_chart(fig2)