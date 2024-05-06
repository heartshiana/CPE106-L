import sqlite3
from tabulate import tabulate

try:
    # Connect to the SQLite database file
    with sqlite3.connect('C:\\Users\\heart\\Documents\\GitHub\\CPE106-L\\LAB5\\Machine Problem 1\\colonialadv.db') as conn:
        print("Connected to the database.")

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Initialize a dictionary to store table information
        table_info = {}

        # Execute SQL queries to fetch table definitions
        tables = ["Participants", "Adventure Class", "Enrolled Participants", "Class"]
        for table_name in tables:
            cursor.execute(f"PRAGMA table_info('{table_name}')")
            table_info[table_name] = cursor.fetchall()

        # Print table definitions in tabular form
        for table_name, columns in table_info.items():
            print(f"\nTable: {table_name}")
            headers = ["Column Name", "Data Type", "Allow NULL", "Primary Key", "Default Value"]
            table_data = [[col[1], col[2], "YES" if col[3] else "NO", "YES" if col[5] else "NO", col[4]] for col in columns]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

except sqlite3.Error as e:
    print("SQLite error:", e)
except Exception as e:
    print("Error:", e)
