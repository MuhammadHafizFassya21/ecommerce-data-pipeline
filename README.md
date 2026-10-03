# 🚀 E-Commerce Data Engineering Pipeline & Analytics Mart

Proyek Data Engineering sederhana yang mengimplementasikan arsitektur *Modern Data Stack* lokal secara *end-to-end* (Extraction, Loading, Transformation, Data Quality Testing, dan Business Intelligence Visualization).

## 🛠️ Tech Stack & Tools
* **Ingestion**: Python (`requests`, `pandas`, `sqlalchemy`)
* **Data Warehouse**: PostgreSQL
* **Transformation & Testing**: dbt-core (`dbt-postgres`)
* **Orchestration**: Python Script (`subprocess`)
* **Visualization**: Streamlit & Plotly

## 🏗️ Architecture Pipeline
1. **Extract & Load**: Mengambil data keranjang belanja (*E-Commerce Carts*) dari REST API dan memuatnya ke PostgreSQL layer `raw_transactions`.
2. **Transform (dbt)**:
   - `stg_transactions`: Cleaning, casting tipe data, dan renaming kolom.
   - `fct_user_orders`: Agregasi metrics total belanja, total pesanan, dan total barang per `user_id`.
3. **Data Quality (dbt test)**: Pengujian otomatis untuk memastikan aturan `not_null` dan `unique`.
4. **BI Dashboard**: Streamlit web dashboard menampilkan KPI ringkasan dan grafik *Top Spenders*.

## ⚡ Cara Menjalankan Pipeline
1. **Clone repository ini**: