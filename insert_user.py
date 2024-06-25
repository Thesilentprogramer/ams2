import sqlite3

# Function to establish database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Connect to the database
conn = get_db_connection()

# Execute ALTER TABLE to add the 'leave_reason' column
try:
    conn.execute('DELETE FROM attendance')
    conn.commit()
    print("Table altered successfully.")
except sqlite3.Error as e:
    print(f"Error while altering table: {e}")

# Close the connection
conn.close()
