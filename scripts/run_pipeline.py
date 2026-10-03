import subprocess
import sys
import os

def run_ingestion():
    """Menjalankan script ekstraksi data dari API ke PostgreSQL."""
    print("==========================================")
    print(" [TAHAP 1/3] Menjalankan Data Ingestion...")
    print("==========================================")
    result = subprocess.run([sys.executable, "scripts/ingest_data.py"], capture_output=False)
    if result.returncode != 0:
        raise Exception("Gagal pada Tahap Ingestion!")

def run_dbt_transform():
    """Menjalankan transformasi dbt."""
    print("\n==========================================")
    print(" [TAHAP 2/3] Menjalankan dbt Transformation...")
    print("==========================================")
    # Pindah ke direktori dbt_project lalu jalankan dbt run
    os.chdir("dbt_project")
    result = subprocess.run(["dbt", "run"], capture_output=False)
    if result.returncode != 0:
        raise Exception("Gagal pada Tahap dbt Transformation!")

def run_dbt_test():
    """Menjalankan validasi kualitas data dbt."""
    print("\n==========================================")
    print(" [TAHAP 3/3] Menjalankan dbt Data Quality Test...")
    print("==========================================")
    result = subprocess.run(["dbt", "test"], capture_output=False)
    if result.returncode != 0:
        raise Exception("Gagal pada Tahap dbt Test!")

if __name__ == "__main__":
    try:
        run_ingestion()
        run_dbt_transform()
        run_dbt_test()
        print("\n==========================================")
        print(" SUCCESS: Entire Pipeline Executed Seamlessly!")
        print("==========================================")
    except Exception as e:
        print(f"\n PIPELINE FAILED: {e}")