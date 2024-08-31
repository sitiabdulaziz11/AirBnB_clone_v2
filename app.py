# app.py or your main test script
from dotenv import load_dotenv
import os
import MySQLdb

# Load environment variables from the .env file
load_dotenv()

# Determine which environment to use
env = os.getenv('APP_ENV', 'development')  # Default to development if not set

if env == 'testing':
    host = os.getenv('HBNB_MYSQL_HOST_TEST')
    user = os.getenv('HBNB_MYSQL_USER_TEST')
    password = os.getenv('HBNB_MYSQL_PWD_TEST')
    database = os.getenv('HBNB_MYSQL_DB_TEST')
else:
    host = os.getenv('HBNB_MYSQL_HOST_DEV')
    user = os.getenv('HBNB_MYSQL_USER_DEV')
    password = os.getenv('HBNB_MYSQL_PWD_DEV')
    database = os.getenv('HBNB_MYSQL_DB_DEV')

# Connect to the database using the chosen environment variables
db = MySQLdb.connect(
    host=host,
    user=user,
    passwd=password,
    db=database
)

print(f"Connecting to MySQL at {host} with user {user} on database {database}")
