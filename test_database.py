# test_database.py

import unittest
import MySQLdb
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class TestMySQLDatabase(unittest.TestCase):
    
    def setUp(self):
        # Connect to the database
        self.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        self.cursor = self.db.cursor()

    def test_insert_state(self):
        """Test inserting a new state into the database."""
        # Step 1: Check the initial count of records in the 'states' table
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        initial_count = self.cursor.fetchone()[0]

        # Step 2: Insert a new record
        self.cursor.execute("INSERT INTO states (name) VALUES ('California');")
        self.db.commit()  # Commit changes

        # Step 3: Check the count again after the insert
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        new_count = self.cursor.fetchone()[0]

        # Step 4: Validate that the count increased by 1
        self.assertEqual(new_count, initial_count + 1, "The state record was not inserted correctly.")

    def tearDown(self):
        # Clean up: Remove the inserted record to keep the test environment clean
        self.cursor.execute("DELETE FROM states WHERE name = 'California';")
        self.db.commit()
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    unittest.main()
