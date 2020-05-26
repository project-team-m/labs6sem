import unittest
from config import DATABASE
from ServicesInterfaces import ManagerInterface
from models import lacksError


class TestManagerClass:
    def __init__(self):
        self.manager = ManagerInterface(**DATABASE)

    def get_processor(self, id_processor=None):
        try:
            return self.manager.get_processor(id_processor)
        except lacksError:
            return 'Processor does not exists.'

    def insert_new_processor(self, **kwargs):
        try:
            self.manager.insert_new_processor(**kwargs)
        except KeyError:
            return 'Fields name and price are required!'

    def remove_processor(self, id_processor=None):
        try:
            self.manager.remove_processor(id_processor)
        except lacksError:
            return 'Processor id has no exist.'

    def update_characteristics(self, id_processor=None, **kwargs):
        try:
            self.manager.update_characteristics(id_processor, **kwargs)
        except lacksError:
            return 'Processor does not exists.'


class UnitTestManagerClass(unittest.TestCase):
    managerInterface = TestManagerClass()

    def test_no_get_processor(self):
        self.assertEqual(self.managerInterface.get_processor(), 'Processor does not exists.')

    def test_no_par_insert_new_processor(self):
        self.assertEqual(self.managerInterface.insert_new_processor(), 'Fields name and price are required!')

    def test_remove_processor(self):
        self.assertEqual(self.managerInterface.remove_processor(), 'Processor id has no exist.')

    def test_no_update_characteristics(self):
        self.assertEqual(self.managerInterface.update_characteristics(), 'Processor does not exists.')


if __name__ == '__main__':
    unittest.main()
