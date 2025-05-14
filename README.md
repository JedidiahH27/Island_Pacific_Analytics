# 🏪 Island Pacific Analytics Dashboard

This is an interactive data analytics dashboard built with **Streamlit** and **Plotly** using simulated retail sales data from a fictional grocery chain, *Island Pacific*.

The goal of this project is to demonstrate my ability to perform **data cleaning**, **exploratory data analysis (EDA)**, and **interactive dashboard development** — with a focus on real-world business insights relevant to roles like:

- Retail Data Analyst  
- Inventory Analyst  
- Business Intelligence Analyst  

---

## 🚀 Features

- **Live dashboard filters** (by store and category)
- **Key performance indicators (KPIs)**:
  - Total sales
  - Units sold
  - Return rate
- **Visual analytics**:
  - Sales trends over time
  - Sales by product category
  - Top 10 products by total revenue
- Clean, modern visuals using **Plotly**

---

## 🧠 What You’ll Learn from This Project

- How product-level data can be used to track performance and inventory needs  
- How to monitor return rates and flag operational issues  
- How category-level and store-level breakdowns help with regional decision-making  
- How interactive dashboards empower non-technical stakeholders  

---

## 📁 Dataset Overview

The dataset is simulated and includes:

| Column Name         | Description                            |
|---------------------|----------------------------------------|
| `date`              | Date of the sale                       |
| `store`             | Store location                         |
| `product`           | Product sold                           |
| `category`          | Product category                       |
| `quantity_sold`     | Number of units sold                   |
| `price_per_unit`    | Price per item                         |
| `discount_applied`  | Discount on the sale                   |
| `total_sales`       | Final revenue from the transaction     |
| `returned`          | Whether the item was returned (0 or 1) |

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** for web app UI
- **Plotly** for interactive charts
- **Pandas** for data wrangling

---

## ▶️ Run It Locally

```bash
git clone https://github.com/JedidiahH27/Island_Pacific_Analytics.git
cd Island_Pacific_Analytics
pip install -r requirements.txt
streamlit run app.py
