# INSERT Command

# Import Sqlite3 library
import sqlite3

# Create the connection
conn = sqlite3.connect("new.db")

# Create the cursor
cursor = conn.cursor()

# Execute the INSERT statement
cursor.execute("INSERT INTO population VALUES('New York City','NY',8400000)")
cursor.execute("INSERT INTO population VALUES('San Francisco','CA',800000)")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
