# src/load_data.py
import sqlite3
import pandas as pd
from pathlib import Path

# Rutas (ajusta si tu estructura es distinta)
RAW_DIR = Path("data/raw")
TRAIN_PATH = RAW_DIR / "train.parquet"
EVAL_PATH  = RAW_DIR / "eval.parquet"
DB_PATH    = Path("data/olist.db")   # archivo .db que NO subiremos a Git

def main():
    print("Leyendo parquet...")
    df_train = pd.read_parquet(TRAIN_PATH)
    df_eval  = pd.read_parquet(EVAL_PATH)

    print(f"Train filas: {len(df_train)}, Eval filas: {len(df_eval)}")

    print(f"Creando DB en {DB_PATH} ...")
    conn = sqlite3.connect(DB_PATH.as_posix())

    print("Guardando tabla 'train'...")
    df_train.to_sql("train", conn, if_exists="replace", index=False)
    print("Guardando tabla 'eval'...")
    df_eval.to_sql("eval", conn, if_exists="replace", index=False)

    conn.close()
    print("Hecho. Base de datos creada:", DB_PATH)

if __name__ == "__main__":
    main()
