import sqlite3

DB_NAME = "battery_data.db"  # Update with your actual database name if different

def read_data():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Query to fetch all records from the WeatherData table
    query = "SELECT * FROM BatteryData"
    cursor.execute(query)
    
    # Fetch all rows from the executed query
    rows = cursor.fetchall()
    
    # Print column names
    column_names = [description[0] for description in cursor.description]
    print(" | ".join(column_names))
    print("-" * 50)
    
    # Print each row
    for row in rows:
        print(row)
    
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    read_data()
