import pandas as pd
from sqlalchemy import create_engine, text
from typing import List, Optional

# Usaremos um banco de dados SQLite em memória para simplificar
DATABASE_URL= "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def initialize_database():
  """Cria as tabelas no banco de dados se não existirem."""
  with engine.connect() as connection:
    connection.execute(text("""
    CREATE TABLE IF NOT EXISTS instruments (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      RptDt DATE,
      TckrSymb TEXT,
      MktNm TEXT,
      SctyCtgyNm TEXT,
      ISIN TEXT,
      CrpnNm TEXT
    );
    """))
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS upload_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            upload_date DATE,
            file_hash TEXT UNIQUE
        );
        """))
