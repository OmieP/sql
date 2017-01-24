# INSERT Command

# Import Sqlite3 library
import sqlite3

# Create the connection
conn = sqlite3.connect("new.db")

# Create the cursor
cursor = conn.cursor()

try:
    # Execute the INSERT statement
    cursor.execute("INSERT INTO populations VALUES('New York City','NY',8400000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco','CA',800000)")

    # Commit the changes
    conn.commit()
except sqlite3.OperationalError:
    print("Oops! Something went wrong")

# Close the connection
conn.close()
