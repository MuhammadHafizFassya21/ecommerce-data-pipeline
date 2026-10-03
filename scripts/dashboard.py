import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# 1. Konfigurasi Halaman Dashboard
st.set_page_config(page_title="E-Commerce Analytics Dashboard", layout="wide")

st.title("📊 E-Commerce Executive Data Mart Dashboard")
st.markdown("Visualisasi Data Mart Agregasi Pelanggan (`analytics.fct_user_orders`)")

# 2. Koneksi ke Database PostgreSQL
DB_URL = "postgresql+psycopg2://postgres:Hafiz2006!@localhost:5432/postgres"

@st.cache_data
def load_data():
    engine = create_engine(DB_URL)
    query = "SELECT * FROM analytics.fct_user_orders;"
    df = pd.read_sql(query, engine)
    return df

try:
    df = load_data()

    # 3. Ringkasan Metrics (KPI Cards)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Active Users", len(df))
    col2.metric("Total Orders Placed", int(df['total_orders'].sum()))
    col3.metric("Total Revenue ($)", f"${df['total_money_spent'].sum():,.2f}")

    st.divider()

    # 4. Grafik Bar Chart: Top 10 User Pengeluaran Tertinggi
    st.subheader("🏆 Top 10 Customers by Total Spend")
    top_users = df.sort_values(by="total_money_spent", ascending=False).head(10)
    
    fig_bar = px.bar(
        top_users,
        x="user_id",
        y="total_money_spent",
        labels={"user_id": "User ID", "total_money_spent": "Total Spent ($)"},
        title="User ID vs Total Spent ($)",
        color="total_money_spent",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # 5. Tabel Data Mentah
    st.subheader("📄 Raw Data Mart Table")
    st.dataframe(df)

except Exception as e:
    st.error(f"Gagal terhubung ke database. Pastikan DB_URL sudah benar. Error: {e}")