import sqlite3
from pathlib import Path

# Get the path to the data folder
data_folder = Path(__file__).parent.parent / "data"

# Create the database file in the data folder
db_path = data_folder / "el_bagel.db"

print(f"Creating database at: {db_path}")

# Connect to the database (this creates the file if it doesn't exist)
conn = sqlite3.connect(db_path)

# Create a cursor - this is what we use to execute SQL commands
cursor = conn.cursor()

# Create the daily_sales table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_sales (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        location TEXT NOT NULL,
        bagel_type TEXT NOT NULL,
        quantity_sold INTEGER NOT NULL,
        quantity_made INTEGER,
        revenue REAL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(date, location, bagel_type)
    )
""")

# Create the events table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        location TEXT,
        expected_impact REAL,
        notes TEXT
    )
""")

# Create the predictions table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY,
        prediction_date TEXT NOT NULL,
        target_date TEXT NOT NULL,
        location TEXT NOT NULL,
        bagel_type TEXT NOT NULL,
        predicted_quantity INTEGER NOT NULL,
        confidence_lower INTEGER,
        confidence_upper INTEGER,
        model_version TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")

# Save the changes
conn.commit()

# Close the connection
conn.close()

print("Database created successfully!")
print("Tables created: daily_sales, events, predictions")