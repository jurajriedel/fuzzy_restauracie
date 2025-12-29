# load_db.py
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Float, String, Table, MetaData

DB_URI = "sqlite:///restaurants.db"

def load(csv_path="restaurants_sample.csv"):
    df = pd.read_csv(csv_path)
    engine = create_engine(DB_URI)
    meta = MetaData()
    restaurants = Table(
        "restaurants", meta,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name", String),
        Column("price", Float),
        Column("rating", Float),
        Column("popularity", Float),
        Column("distance", Float),
        Column("cuisine", String)
    )
    meta.create_all(engine)
    df.to_sql("restaurants", engine, if_exists="replace", index=False)
    print("Dáta importované do restaurants.db (tabulka restaurants).")

if __name__ == "__main__":
    load()
