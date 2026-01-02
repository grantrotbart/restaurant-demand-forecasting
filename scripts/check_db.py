import sqlite3
from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
db_path = data_folder / "el_bagel.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Count rows in each table
cursor.execute("SELECT COUNT(*) FROM daily_sales")
sales_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM events")
events_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM predictions")
predictions_count = cursor.fetchone()[0]

print(f"daily_sales: {sales_count} rows")
print(f"events: {events_count} rows")
print(f"predictions: {predictions_count} rows")

# Show the actual sales data
print("\n--- Sales Data ---")
cursor.execute("SELECT date, location, bagel_type, quantity_sold FROM daily_sales")
for row in cursor.fetchall():
    print(row)

conn.close()