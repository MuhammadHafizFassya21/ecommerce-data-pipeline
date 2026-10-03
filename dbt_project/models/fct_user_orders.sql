-- Model Fact Table: Menghitung ringkasan transaksi per pengguna (User)
WITH clean_transactions AS (
    -- Mengambil data yang SUDAH DIBERSIHKAN dari model stg_transactions sebelumnya
    SELECT * FROM {{ ref('stg_transactions') }}
)

SELECT
    user_id,
    COUNT(DISTINCT cart_id) AS total_orders,
    SUM(total_quantity) AS total_items_bought,
    SUM(total_amount) AS total_money_spent
FROM clean_transactions
GROUP BY user_id