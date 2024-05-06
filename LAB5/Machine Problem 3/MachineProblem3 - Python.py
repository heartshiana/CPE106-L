import sqlite3
from tabulate import tabulate

# Define the SQL statements
sql_statements = """
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "ADVENTURE_TRIP" (
    "TRIP_ID"    DECIMAL,
    "TRIP_NAME"  VARCHAR(75),
    "START_LOCATION"  CHAR(50),
    "STATE"  CHAR(2),
    "DISTANCE"  NUMBER(10, 2),
    "MAX_GRP_SIZE"  NUMBER(10, 2),
    "TYPE"  CHAR(20),
    "SEASON"  CHAR(20)
);
INSERT INTO "ADVENTURE_TRIP" VALUES (45, 'Jaye Peak', 'Jay', 'VT', 8, 8, 'Hiking', 'Summer');
COMMIT;
"""

# Database file path
db_file = "adventure_trip.db"

try:
    # Connect to the SQLite database file
    with sqlite3.connect(db_file) as conn:
        print("Connected to the database.")

        # Execute the SQL statements
        conn.executescript(sql_statements)

        # Fetch the table data
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ADVENTURE_TRIP")
        rows = cursor.fetchall()

        # Convert table data to a list of lists for tabulate
        table_data = [list(row) for row in rows]

        # Print the table data in tabular format
        print("\nADVENTURE_TRIP Table:")
        headers = ["TRIP_ID", "TRIP_NAME", "START_LOCATION", "STATE", "DISTANCE", "MAX_GRP_SIZE", "TYPE", "SEASON"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

except sqlite3.Error as e:
    print("SQLite error:", e)
except Exception as e:
    print("Error:", e)
