from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
# from models.user import User
# from models.place import Place
from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review

# from dotenv import load_dotenv

# # Load environment variables from the .env file
# load_dotenv()

# classes = [State, City, User, Place, Review, Amenity]
classes = [State]

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database engine
        """
        # user = getenv('HBNB_MYSQL_USER')
        # pwd = getenv('HBNB_MYSQL_PWD')
        # host = getenv('HBNB_MYSQL_HOST')
        # db = getenv('HBNB_MYSQL_DB')
        
        # self.__engine = create_engine(
        #     f"mysql+mysqldb://{user}:{pwd}@{host}/{db}", pool_pre_ping=True) or below
        
        self.__engine = create_engine(
            f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}:{getenv('HBNB_MYSQL_PWD')}@{getenv('HBNB_MYSQL_HOST')}/{getenv('HBNB_MYSQL_DB')}", pool_pre_ping=True)
        
        # Drop all tables if in test environmen
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        else:
            # Attempt to create all tables
            try:
                Base.metadata.create_all(self.__engine)
                print("Tables created successfully.")
            except Exception as e:
                print(f"Error creating tables: {e}")
        
    def all(self, cls=None):
        """Returns a dictionary of models in the database
        """
        objs = {}
        if cls and cls in classes:
            for obj in self.__session.query(cls).all():
                key = obj.__class__.__name__ + '.' + obj.id
                objs[key] = obj
        else:
            for cls in Base.registry._class_registry.values():
                if hasattr(cls, '__table__'):
                    for obj in self.__session.query(cls).all():
                        key = obj.__class__.__name__ + '.' + obj.id
                        objs[key] = obj
        return objs

    def new(self, obj):
        """Adds a new object to the database
        """
        self.__session.add(obj)

    def save(self):
        """Saves all changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the database
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and starts
        a new session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the database session
        """
        self.__session.remove()
        