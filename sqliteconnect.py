#!/usr/bin/env python
"""
SQLite Database Connection and Table Creation Script
For MCC Portal Project
"""
import sqlite3
import os
from pathlib import Path

# Database path
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'mcc_portal' / 'db.sqlite3'

class SQLiteConnection:
    """SQLite Database Connection Class"""
    
    def __init__(self, db_path=None):
        self.db_path = db_path or DB_PATH
        self.connection = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            print(f"✅ Connected to database: {self.db_path}")
            return self.connection
        except sqlite3.Error as e:
            print(f"❌ Error connecting to database: {e}")
            return None
    
    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("🔒 Database connection closed")
    
    def execute_query(self, query, params=None):
        """Execute a single query"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print(f"✅ Query executed successfully")
            return cursor
        except sqlite3.Error as e:
            print(f"❌ Error executing query: {e}")
            return None
    
    def fetch_all(self, query, params=None):
        """Fetch all results from query"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Error fetching data: {e}")
            return None

def create_tables():
    """Create all necessary tables for MCC Portal"""
    db = SQLiteConnection()
    
    if not db.connect():
        return False
    
    try:
        # Create Citizens Table
        create_citizens_table = """
        CREATE TABLE IF NOT EXISTS citizens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(15) UNIQUE NOT NULL,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        # Create Officers Table
        create_officers_table = """
        CREATE TABLE IF NOT EXISTS officers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            department VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        # Create Complaints Table
        create_complaints_table = """
        CREATE TABLE IF NOT EXISTS complaints (
            complaint_id INTEGER PRIMARY KEY AUTOINCREMENT,
            citizen_id INTEGER NOT NULL,
            department VARCHAR(100) NOT NULL,
            title VARCHAR(200) NOT NULL,
            address VARCHAR(300) NOT NULL,
            description TEXT NOT NULL,
            map_location VARCHAR(100),
            attachment VARCHAR(255),
            status VARCHAR(20) DEFAULT 'Pending',
            date_submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            officer_remark TEXT,
            FOREIGN KEY (citizen_id) REFERENCES citizens(id)
        );
        """
        
        # Create Admin Users Table
        create_admin_table = """
        CREATE TABLE IF NOT EXISTS admin_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            is_staff BOOLEAN DEFAULT 1,
            is_superuser BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        # Execute table creation
        tables = [
            ("Citizens", create_citizens_table),
            ("Officers", create_officers_table),
            ("Complaints", create_complaints_table),
            ("Admin Users", create_admin_table)
        ]
        
        for table_name, query in tables:
            db.execute_query(query)
            print(f"✅ {table_name} table created/verified")
        
        # Create indexes for better performance
        indexes = [
            "CREATE INDEX IF NOT EXISTS idx_citizens_email ON citizens(email);",
            "CREATE INDEX IF NOT EXISTS idx_citizens_username ON citizens(username);",
            "CREATE INDEX IF NOT EXISTS idx_officers_department ON officers(department);",
            "CREATE INDEX IF NOT EXISTS idx_complaints_status ON complaints(status);",
            "CREATE INDEX IF NOT EXISTS idx_complaints_department ON complaints(department);",
            "CREATE INDEX IF NOT EXISTS idx_complaints_citizen ON complaints(citizen_id);"
        ]
        
        for index_query in indexes:
            db.execute_query(index_query)
        
        print("✅ All indexes created")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        return False
    finally:
        db.close()

def insert_sample_data():
    """Insert sample data into tables"""
    db = SQLiteConnection()
    
    if not db.connect():
        return False
    
    try:
        # Sample Citizens
        citizens_data = [
            ('John Doe', 'john@example.com', '+919876543210', 'johndoe', 'password123'),
            ('Jane Smith', 'jane@example.com', '+919876543211', 'janesmith', 'password123'),
            ('Bob Wilson', 'bob@example.com', '+919876543212', 'bobwilson', 'password123')
        ]
        
        for citizen in citizens_data:
            query = "INSERT OR IGNORE INTO citizens (name, email, phone, username, password) VALUES (?, ?, ?, ?, ?)"
            db.execute_query(query, citizen)
        
        # Sample Officers
        officers_data = [
            ('Ravi Kumar', 'ravi@mcc.gov.in', 'ravikumar', 'pass123', 'Sanitation'),
            ('Suresh Shetty', 'suresh@mcc.gov.in', 'suressh', 'pass123', 'Roads & Infrastructure'),
            ('Anitha Rao', 'anitha@mcc.gov.in', 'anitha', 'pass123', 'Water Supply')
        ]
        
        for officer in officers_data:
            query = "INSERT OR IGNORE INTO officers (name, email, username, password, department) VALUES (?, ?, ?, ?, ?)"
            db.execute_query(query, officer)
        
        # Sample Complaints
        complaints_data = [
            (1, 'Sanitation', 'Garbage Collection Issue', 'Main Street', 'Garbage not collected for 3 days', 'Pending'),
            (2, 'Water Supply', 'Pipe Leakage', '123 Main Street', 'Water leaking from pipe', 'In Progress'),
            (3, 'Roads & Infrastructure', 'Pothole Issue', 'Highway Road', 'Large pothole causing accidents', 'Pending')
        ]
        
        for complaint in complaints_data:
            query = "INSERT OR IGNORE INTO complaints (citizen_id, department, title, address, description, status) VALUES (?, ?, ?, ?, ?, ?)"
            db.execute_query(query, complaint)
        
        print("✅ Sample data inserted successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error inserting sample data: {e}")
        return False
    finally:
        db.close()

def view_tables():
    """View all tables and their data"""
    db = SQLiteConnection()
    
    if not db.connect():
        return
    
    try:
        # Get all table names
        tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = db.fetch_all(tables_query)
        
        print("\n📊 Available Tables:")
        for table in tables:
            table_name = table[0]
            print(f"\n🔹 {table_name.upper()}")
            
            # Get table schema
            schema_query = f"PRAGMA table_info({table_name});"
            schema = db.fetch_all(schema_query)
            print("Columns:", [col[1] for col in schema])
            
            # Get row count
            count_query = f"SELECT COUNT(*) FROM {table_name};"
            count = db.fetch_all(count_query)[0][0]
            print(f"Rows: {count}")
            
            # Show sample data (first 3 rows)
            if count > 0:
                data_query = f"SELECT * FROM {table_name} LIMIT 3;"
                data = db.fetch_all(data_query)
                print("Sample data:")
                for row in data:
                    print(f"  {row}")
        
    except Exception as e:
        print(f"❌ Error viewing tables: {e}")
    finally:
        db.close()

def main():
    """Main function to run database operations"""
    print("🚀 MCC Portal Database Setup")
    print("=" * 50)
    
    # Create tables
    if create_tables():
        print("\n📝 Tables created successfully!")
        
        # Insert sample data
        if insert_sample_data():
            print("\n📊 Sample data inserted successfully!")
        
        # View tables
        print("\n👀 Viewing database structure...")
        view_tables()
        
        print("\n✅ Database setup completed!")
    else:
        print("\n❌ Database setup failed!")

if __name__ == "__main__":
    main()