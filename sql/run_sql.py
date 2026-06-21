import os
import sqlite3
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(SCRIPT_DIR, "..", "data", "processed", "cleaned_covid_data.csv")

print(f"Loading file: {csv_path}")

# 1. Load data
df = pd.read_csv(csv_path)

# AUTOMATIC FIX: Clean the column names so they match your SQL perfectly
df.columns = [c.strip().replace("/", "_").replace(" ", "_") for c in df.columns]

# 2. Setup database table
conn = sqlite3.connect(":memory:")
df.to_sql("covid_data", conn, index=False, if_exists="replace")

# 3. Read and run queries from your covid_analysis.sql file
sql_path = os.path.join(SCRIPT_DIR, "covid_analysis.sql")
with open(sql_path, "r") as f:
    queries = f.read().split(";")

for query in queries:
    query = query.strip()
    if query:
        print("\n" + "="*40)
        print(f"Running Query:\n{query}")
        try:
            result = pd.read_sql_query(query, conn)
            print(result)
        except Exception as e:
            print(f"Error running this query: {e}")

conn.close()
