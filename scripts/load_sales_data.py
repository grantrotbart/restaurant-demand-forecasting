import sqlite3
import csv
from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
db_path = data_folder / "el_bagel.db"


def load_sales_from_csv(csv_path):
    """Load sales data from a CSV file into the database."""
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        
        rows_loaded = 0
        for row in reader:
            cursor.execute("""
                INSERT OR REPLACE INTO daily_sales 
                (date, location, bagel_type, quantity_sold, quantity_made, revenue)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                row['date'],
                row['location'],
                row['bagel_type'],
                int(row['quantity_sold']),
                int(row['quantity_made']) if row.get('quantity_made') else None,
                float(row['revenue']) if row.get('revenue') else None
            ))
            rows_loaded += 1
    
    conn.commit()
    conn.close()
    
    print(f"Loaded {rows_loaded} rows from {csv_path}")


if __name__ == "__main__":
    # For now, we'll test with a sample file
    sample_path = data_folder / "sample_sales.csv"
    
    if sample_path.exists():
        load_sales_from_csv(sample_path)
    else:
        print(f"No file found at {sample_path}")
        print("Once you have real data, put it in the data folder and update this script.")