import requests
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text

# Gunakan koneksi ke PostgreSQL lokal pgAdmin Anda (atau sesuai settingan Anda)
# Jika pakai pgAdmin lokal, ganti postgres:password_anda@localhost:5432/postgres
# Format: postgresql+psycopg2://USER_PGADMIN:PASSWORD_PGADMIN@localhost:5432/NAMA_DATABASE
DB_URL = "postgresql+psycopg2://postgres:Hafiz2006!@localhost:5432/postgres"

def fetch_api_data():
    """Mengambil data transaksi mentah dari DummyJSON API."""
    print(" Mengambil data dari API...")
    url = "https://dummyjson.com/carts"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(" Berhasil mengambil data dari API!")
        return response.json()['carts']
    else:
        raise Exception(f"Gagal mengambil data. Status code: {response.status_code}")

def transform_to_raw_df(json_data):
    """Mengubah data JSON menjadi Pandas DataFrame terstruktur."""
    print(" Flattening data JSON...")
    raw_records = []
    for cart in json_data:
        cart_id = cart['id']
        user_id = cart['userId']
        for item in cart['products']:
            raw_records.append({
                'cart_id': cart_id,
                'user_id': user_id,
                'product_id': item['id'],
                'product_title': item['title'],
                'price': item['price'],
                'quantity': item['quantity'],
                'total': item['total']
            })
    
    df = pd.DataFrame(raw_records)
    print(f" Total baris data mentah yang didapat: {len(df)}")
    return df

def load_to_postgres(df):
    """Menyimpan DataFrame ke layer database raw_transactions tanpa menghapus tabel."""
    print(" Menghubungkan ke PostgreSQL...")
    engine = create_engine(DB_URL)
    
    with engine.begin() as connection:
        # 1. Buat tabel jika belum ada
        df.head(0).to_sql('raw_transactions', connection, if_exists='append', index=False)
        # 2. Kosongkan isi data lama tanpa merusak dependensi View dbt
        connection.execute(text("TRUNCATE TABLE raw_transactions CASCADE;"))
        # 3. Masukkan data terbaru
        df.to_sql('raw_transactions', connection, if_exists='append', index=False)
        
    print(" Selesai! Data mentah berhasil dimasukkan ke tabel 'raw_transactions'.")
    
if __name__ == "__main__":
    data_json = fetch_api_data()
    df_raw = transform_to_raw_df(data_json)
    load_to_postgres(df_raw)