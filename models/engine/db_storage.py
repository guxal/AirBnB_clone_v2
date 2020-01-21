#!/usr/bin/python3
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def create_dict(_dict, obj):
    for o in obj:
        key = "{}.{}".format(type(o).__name__, o.id)
        value = o
        _dict[key] = value


class DBStorage:
    __engine = None
    __session = None
    cities = relationship("City")

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(environ.get('HBNB_MYSQL_USER'),
                                              environ.get('HBNB_MYSQL_PWD'),
                                              environ.get('HBNB_MYSQL_HOST'),
                                              environ.get('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Select all objects of a cls
        """
        sess = self.__session
        _dict = dict()
        my_list = ['State', 'User', 'City', 'Place', 'Review', 'Amenity']

        if cls is None:
            for cls in my_list:
                session = sess.query(eval(cls)).all()
                create_dict(_dict, session)
        else:
            session = sess.query(eval(cls)).all()
            create_dict(_dict, session)
        return _dict

    def new(self, obj):
        """Add obj to the database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj if not none
        """
        if obj is not None:
            del obj

    def reload(self):
        """Update obj
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """
        """
        self.__session.remove()
