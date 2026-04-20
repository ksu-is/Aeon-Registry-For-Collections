import mysql.connector

def get_connection():
    """Establish connection to your local MySQL server."""
    # NOTE: Replace 'your_password' with your actual MySQL password!
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="73838", 
        database="aeon_registry"
    )

def create_table():
    """Creates the specimen table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS specimens (
            id INT AUTO_INCREMENT PRIMARY KEY,
            common_name VARCHAR(100),
            scientific_name VARCHAR(100),
            location VARCHAR(255),
            details TEXT,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_specimen(name, sci, loc, details):
    """Saves a new finding into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO specimens (common_name, scientific_name, location, details) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, sci, loc, details))
    conn.commit()
    conn.close()
