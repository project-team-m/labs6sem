from abc import ABC, abstractclassmethod
from DAO_Models import Processor
from models import lacksError
from sqlalchemy.orm import sessionmaker
from config import DATABASE
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine


class IManagerService(ABC):
    @abstractclassmethod
    def get_processor(cls, id_processor):
        pass

    @abstractclassmethod
    def insert_new_processor(cls, **kwargs):
        pass

    @abstractclassmethod
    def remove_processor(cls, id_processor):
        pass

    @abstractclassmethod
    def update_characteristics(cls, id_processor, **kwargs):
        pass


class ManagerInterface(IManagerService):
    def __init__(self, **kwargs):
        self.__session = sessionmaker(bind=create_engine(URL(**kwargs), echo=False))()

    def get_processor(self, id_processor):
        proc = self.__session.query(Processor).filter(Processor.id == id_processor).first()
        if not proc:
            raise lacksError("Processor does not exists")
        else:
            return proc

    def insert_new_processor(self, **kwargs):
        a = Processor(**kwargs)
        self.__session.add(a)
        self.__session.commit()

    def remove_processor(self, id_processor):
        self.__session.delete(self.get_processor(id_processor))
        self.__session.commit()

    def update_characteristics(self, id_processor, **kwargs):
        a = self.get_processor(id_processor)
        a.update_characteristics(**kwargs)
        self.__session.commit()


class ManagerClass:
    def __init__(self, config=DATABASE):
        self.manager = ManagerInterface(**config)

    def get_processor(self, id_processor=None):
        try:
            print(self.manager.get_processor(id_processor))
        except lacksError:
            print('Processor does not exists.')

    def insert_new_processor(self, **kwargs):
        try:
            self.manager.insert_new_processor(**kwargs)
        except KeyError:
            print('Fields name and price are required!')

    def remove_processor(self, id_processor=None):
        try:
            self.manager.remove_processor(id_processor)
        except TypeError:
            print('Processor id has no exist.')

    def update_characteristics(self, id_processor=None, **kwargs):
        try:
            self.manager.update_characteristics(id_processor, **kwargs)
        except TypeError:
            print('Processor id has no exist.')
        except lacksError:
            print('Processor does not exists.')


if __name__ == '__main__':
    a = ManagerClass()
    a.get_processor(99)
