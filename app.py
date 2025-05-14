import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv("data/island_pacific_sales.csv", parse_dates=["date"])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("📊 Filter Data")
store_filter = st.sidebar.multiselect("Select Store", options=df["store"].unique(), default=df["store"].unique())
category_filter = st.sidebar.multiselect("Select Category", options=df["category"].unique(), default=df["category"].unique())

filtered_df = df[(df["store"].isin(store_filter)) & (df["category"].isin(category_filter))]

# KPIs
total_sales = filtered_df["total_sales"].sum()
units_sold = filtered_df["quantity_sold"].sum()
return_rate = (filtered_df["returned"].sum() / units_sold) * 100 if units_sold > 0 else 0

st.title("🏪 Island Pacific Sales Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("💵 Total Sales", f"${total_sales:,.2f}")
col2.metric("📦 Units Sold", f"{int(units_sold)}")
col3.metric("↩️ Return Rate", f"{return_rate:.2f}%")

st.markdown("---")

# Sales over time
sales_by_date = (
    filtered_df.groupby("date")["total_sales"]
    .sum()
    .reset_index()
    .sort_values("date")
)

fig1 = px.line(
    sales_by_date,
    x="date",
    y="total_sales",
    title="📈 Total Sales Over Time",
    labels={"total_sales": "Sales ($)", "date": "Date"},
    template="plotly_white"
)
st.plotly_chart(fig1, use_container_width=True)

# Sales by Category
sales_by_category = (
    filtered_df.groupby("category")["total_sales"]
    .sum()
    .reset_index()
    .sort_values("total_sales", ascending=False)
)

fig2 = px.bar(
    sales_by_category,
    x="total_sales",
    y="category",
    orientation="h",
    title="📦 Sales by Category",
    labels={"total_sales": "Sales ($)", "category": "Product Category"},
    template="plotly_white"
)
st.plotly_chart(fig2, use_container_width=True)

# Top Products
top_products = (
    filtered_df.groupby("product")["total_sales"]
    .sum()
    .reset_index()
    .sort_values("total_sales", ascending=False)
    .head(10)
)

fig3 = px.bar(
    top_products,
    x="total_sales",
    y="product",
    orientation="h",
    title="🏆 Top 10 Products by Sales",
    labels={"total_sales": "Sales ($)", "product": "Product"},
    template="plotly_white"
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.caption("Made by Jedidiah Hernandez | [GitHub](https://github.com/JedidiahH27) | [LinkedIn](https://linkedin.com/in/jedidiah-hernandez)")
