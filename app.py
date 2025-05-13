import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit style
st.set_page_config(page_title="Island Pacific Dashboard", layout="wide")
st.title("📊 Island Pacific Sales Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/island_pacific_sales.csv", parse_dates=["date"])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔎 Filters")
store = st.sidebar.multiselect("Select Store", options=df['store'].unique(), default=df['store'].unique())
category = st.sidebar.multiselect("Select Category", options=df['category'].unique(), default=df['category'].unique())

# Filtered DataFrame
filtered_df = df[(df['store'].isin(store)) & (df['category'].isin(category))]

# KPI Section
total_sales = filtered_df['total_sales'].sum()
total_units = filtered_df['quantity_sold'].sum()
return_rate = filtered_df['returned'].sum() / filtered_df['quantity_sold'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Revenue", f"${total_sales:,.2f}")
col2.metric("📦 Total Units Sold", f"{total_units:,}")
col3.metric("↩️ Return Rate", f"{return_rate:.2%}")

st.markdown("---")

# Time Series Sales
st.subheader("🕒 Sales Over Time")
sales_by_date = filtered_df.groupby("date")['total_sales'].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(data=sales_by_date, x='date', y='total_sales', ax=ax)
ax.set_title("Total Sales Over Time")
ax.set_ylabel("Sales ($)")
st.pyplot(fig)

st.markdown("---")

# Sales by Category
st.subheader("📁 Sales by Category")
sales_by_cat = filtered_df.groupby("category")['total_sales'].sum().sort_values(ascending=False)

fig2, ax2 = plt.subplots()
sns.barplot(x=sales_by_cat.values, y=sales_by_cat.index, palette="viridis", ax=ax2)
ax2.set_xlabel("Sales ($)")
st.pyplot(fig2)

# Top Products
st.subheader("🏆 Top 10 Products by Revenue")
top_products = (
    filtered_df.groupby("product")["total_sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig3, ax3 = plt.subplots()
sns.barplot(x=top_products.values, y=top_products.index, palette="mako", ax=ax3)
ax3.set_xlabel("Sales ($)")
st.pyplot(fig3)
