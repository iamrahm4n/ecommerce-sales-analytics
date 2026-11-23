import pandas as pd
import sqlite3

# Load CSV dataset
file_path = "data/raw/Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Create database connection
database_path = "data/processed/superstore.db"
conn = sqlite3.connect(database_path)

# Load data into SQLite table
df.to_sql("superstore", conn, if_exists="replace", index=False)

# Verify database
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM superstore")
row_count = cursor.fetchone()[0]

print(f"Database created successfully!")
print(f"Total records loaded: {row_count}")

# Close connection
conn.close()