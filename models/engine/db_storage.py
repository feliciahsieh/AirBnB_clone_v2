#!/usr/bin/python3                                                             
"""create the engine"""

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    '''storage of class insts like one from filestorage'''
    __engine = None
    __session = None

    def __init__(self):
        '''Create the engine'''
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ.get('HBNB_MYSQL_USER'),
                os.environ.get('HBNB_MYSQL_PWD'),
                os.environ.get('HBNB_MYSQL_HOST'),
                os.environ.get('HBNB_MYSQL_DB')))
        if get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''dictionary like FileStorage Method'''

    def new(self, obj):
        '''Add object to current database session'''

    def save(self):
        '''commit all changes of the current database session'''

    def delete(self, obj=None):
        '''delete from the current database session'''

    def reload(self):
        '''create all tables in the database'''
