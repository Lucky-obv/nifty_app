import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Nifty_Stocks.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Title
st.title("📈 Nifty Stocks Explorer")

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Category selection
categories = df['Category'].unique()
selected_category = st.selectbox("Select Category:", categories)

# Filter by category
filtered_category = df[df['Category'] == selected_category]

# Symbol selection
symbols = filtered_category['Symbol'].unique()
selected_symbol = st.selectbox("Select Symbol:", symbols)

# Filter by symbol
filtered_symbol = filtered_category[filtered_category['Symbol'] == selected_symbol]

# Plot
st.subheader(f"Stock Trend for {selected_symbol}")
fig, ax = plt.subplots(figsize=(10, 5))
sb.lineplot(data=filtered_symbol, x="Date", y="Close", ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
