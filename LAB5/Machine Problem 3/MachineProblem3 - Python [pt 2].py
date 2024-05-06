import sqlite3
from tabulate import tabulate

# Database file path
db_file = "DandE.db"

try:
    # Connect to the SQLite database file
    with sqlite3.connect(db_file) as conn:
        print("Connected to the database.")

        # Fetch the data from the tables
        cursor = conn.cursor()

        # Fetch data from GUIDE table
        cursor.execute("SELECT * FROM GUIDE")
        guide_rows = cursor.fetchall()

        # Fetch data from CUSTOMER table
        cursor.execute("SELECT * FROM CUSTOMER")
        customer_rows = cursor.fetchall()

        # Fetch data from RESERVATION table
        cursor.execute("SELECT * FROM RESERVATION")
        reservation_rows = cursor.fetchall()

        # Fetch data from TRIP table
        cursor.execute("SELECT * FROM TRIP")
        trip_rows = cursor.fetchall()

        # Fetch data from TRIP_GUIDES table
        cursor.execute("SELECT * FROM TRIP_GUIDES")
        trip_guides_rows = cursor.fetchall()

        # Print the tables in tabular format
        print("\nGUIDE Table:")
        print(tabulate(guide_rows, headers=[i[0] for i in cursor.description], tablefmt="grid"))

        print("\nCUSTOMER Table:")
        print(tabulate(customer_rows, headers=[i[0] for i in cursor.description], tablefmt="grid"))

        print("\nRESERVATION Table:")
        print(tabulate(reservation_rows, headers=[i[0] for i in cursor.description], tablefmt="grid"))

        print("\nTRIP Table:")
        print(tabulate(trip_rows, headers=[i[0] for i in cursor.description], tablefmt="grid"))

        print("\nTRIP_GUIDES Table:")
        print(tabulate(trip_guides_rows, headers=[i[0] for i in cursor.description], tablefmt="grid"))

except sqlite3.Error as e:
    print("SQLite error:", e)
except Exception as e:
    print("Error:", e)
