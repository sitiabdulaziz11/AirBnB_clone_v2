# # app.py or your main test script
# from dotenv import load_dotenv
# import os
# import MySQLdb

# # Load environment variables from the .env file
# load_dotenv()

# # Determine which environment to use
# env = os.getenv('APP_ENV', 'development')  # Default to development if not set

# if env == 'testing':
#     host = os.getenv('HBNB_MYSQL_HOST_TEST')
#     user = os.getenv('HBNB_MYSQL_USER_TEST')
#     password = os.getenv('HBNB_MYSQL_PWD_TEST')
#     database = os.getenv('HBNB_MYSQL_DB_TEST')
# else:
#     host = os.getenv('HBNB_MYSQL_HOST_DEV')
#     user = os.getenv('HBNB_MYSQL_USER_DEV')
#     password = os.getenv('HBNB_MYSQL_PWD_DEV')
#     database = os.getenv('HBNB_MYSQL_DB_DEV')

# # Connect to the database using the chosen environment variables
# db = MySQLdb.connect(
#     host=host,
#     user=user,
#     passwd=password,
#     db=database
# )

# print(f"Connecting to MySQL at {host} with user {user} on database {database}")

#!/usr/bin/python3
"""
Main entry point for the application.
"""

from models import storage
from models.state import State
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


def setup_storage():
    """Set up the storage engine by reloading it."""
    # storage.reload()


def create_sample_data():
    """Create sample data for testing purposes."""
    # Example: Add a State to the database
    new_state = State(name="California")
    storage.new(new_state)
    storage.save()
    print("Sample data created.")


def main():
    """Main function to run the application."""
    # Set up storage and load tables
    setup_storage()

    # Optional: Create sample data
    create_sample_data()

    # Print confirmation
    print("Application has been set up successfully.")


if __name__ == "__main__":
    main()
