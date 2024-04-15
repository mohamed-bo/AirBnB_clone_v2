#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_if_empty(self):
        """_summary_
        """
        self.assertEqual(len(storage.all()), 0)

    def test_gdid_create(self):
        """_summary_
        """
        gdid = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all_func(self):
        """_summary_
        """
        gdid = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_init_fro_basemodel(self):
        """_summary_
        """
        gdid = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_without_any_thing(self):
        """_summary_
        """
        gdid = BaseModel()
        gdid_dic = gdid.to_dict()
        gdid.save()
        gdid2 = BaseModel(**gdid_dic)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_to_save(self):
        """ FileStorage save method """
        gdid = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        gdid = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(gdid.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """_summary_
        """
        try:
            with open('file.json', 'w') as f:
                pass
            with self.assertRaises(ValueError):
                storage.reload()
        except Exception:
            pass

    def test_reload_as_none(self):
        """_summary_
        """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        gdid = BaseModel()
        gdid.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_if_str(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_atrr(self):
        """ Key is properly formatted """
        gdid = BaseModel()
        _id = gdid.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_typeof_storage(self):
        """_summary_
        """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)
