#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv
# from dotenv import load_dotenv

# # Load environment variables from the .env file
# load_dotenv()

# from models.engine.db_storage import DBStorage
# from models.engine.file_storage import FileStorage, these imports case issue when running

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
