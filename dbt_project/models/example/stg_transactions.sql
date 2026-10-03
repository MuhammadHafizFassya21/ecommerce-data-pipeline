WITH source_data AS (
    SELECT * FROM {{ source('public', 'raw_transactions') }}
)

SELECT
    cart_id,
    user_id,
    product_id,
    product_title AS product_name,
    CAST(price AS NUMERIC(10, 2)) AS unit_price,
    CAST(quantity AS INT) AS total_quantity,
    CAST(total AS NUMERIC(10, 2)) AS total_amount
FROM source_data