#!/usr/bin/python3
import os
import sys
from sqlalchemy import  create_engine
from sqlalchemy import create_engine, URL
from sqlalchemy import MetaData
from models.base_model import Base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        url_obj = URL.create(
            drivername='mysql+mysqldb',
            username=os.getenv('HBNB_MYSQL_USER'),
            password=os.getenv('HBNB_MYSQL_PWD'),
            host=os.getenv('HBNB_MYSQL_NYSQL_HOST'),
            database=os.getenv('HBNB_MYSQL_DB'),
            port=3306
            )
        self.__engine = create_engine(url_obj,pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData()
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        res = dict()
        classes = []
        if cls == None:
            metadata = MetaData()
            for el in metadata.tables.values():
                classes.append(el.__class__.__name__)
        else:
            classes.append(cls)
        for obj in classes:
            res.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        return res

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        try:
            self.__session.commit()
        except SQLAlchemyError as msg:
            print(f"SQLAlchemyError: {msg}")
            self.__session.rollback()

    def delete(self, obj=None):
        if obj != None:
            element = obj.__class__.__name__
            try:
                self.__session.query(element).filter(element.id ==
                obj.id).one()
                self.__session.delete()
            except SQLAlchemyError as msg:
                print(f"SQLAlchemyError: {msg}")

    def reload(self):
        try:
            Base.metadata.create_all(self.__engine)
            Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = Session()
        except SQLAlchemyError as msg:
            sys.exit(f"SQLAlchemyError: {msg}")
        finally:
            if self.__session:
                self.__session.close()
