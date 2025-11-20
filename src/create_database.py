import pandas as pd
import sqlite3
from pathlib import Path

# Rutas importantes
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
DB_FILE = PROCESSED_DIR / "olist.db"

def create_database():
    # Crear carpeta processed si no existe
    PROCESSED_DIR.mkdir(exist_ok=True)

    # Crear conexión a la base de datos
    conn = sqlite3.connect(DB_FILE)

    # Parquet files
    parquet_files = list(RAW_DIR.glob("*.parquet"))

    print("Archivos encontrados:", parquet_files)

    for file in parquet_files:
        # Nombre de la tabla = nombre del archivo sin extensión
        table_name = file.stem

        print(f"Cargando {file.name} en la tabla {table_name}...")

        df = pd.read_parquet(file)
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()
    print(f"Base de datos creada en: {DB_FILE}")

if __name__ == "__main__":
    create_database()
