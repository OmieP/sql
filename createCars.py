# Import SQLite3
import sqlite3

# Create the database
conn = sqlite3.connect("cars.db")

# Get the cursor
c = conn.cursor()

# Insert the columns
c.execute("""CREATE TABLE inventory(Make TEXT, Model TEXT, Quantity INT)""")

c.close()
