from dependency_injector import providers, containers
from DAO_Models import Processor
from models import lacksError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from config import DATABASE


class Config:
    count = 0

    def __init__(self, cfg):
        Config.count += 1
        self.cfg = cfg


class ManagerInterface:
    def __init__(self, cfg):
        self.__session = sessionmaker(bind=create_engine(URL(**cfg), echo=False))()

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


class ManagerProvider:
    cfg = providers.Singleton(Config, cfg=DATABASE)
    manager = providers.Singleton(ManagerInterface, cfg=cfg().cfg)()

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

    def get_count(self):
        print(self.cfg().count)


if __name__ == '__main__':
    manager = providers.Singleton(ManagerProvider)
    manager2 = providers.Singleton(ManagerProvider)
    manager3 = providers.Singleton(ManagerProvider)

    manager3().get_count()

    manager().get_processor(1)
