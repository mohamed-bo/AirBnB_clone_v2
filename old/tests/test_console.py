#!/usr/bin/python3
""" unit test for the console cli
"""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """testing the console cli

    Args:
        unittest (unittest): unittest class
    """

    @classmethod
    def setUpClass(to_bes_tested):
        """setting up the class
        """
        try:
            os.rename("file.json", "tmp")
        except Exception:
            pass

        to_bes_tested.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(to_bes_tested):
        """tearing dowen

        Args:
            to_bes_tested (CabseModel): Base model as a perent
        """
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del to_bes_tested.HBNB

    def setUp(self):
        """Reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_error_creation(self):
        """testing error in create
        """
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", file.getvalue())

    def test_Validation_for_create(self):
        """Validation
        """
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create BaseModel")
            try:
                base_m = file.getvalue().strip()
            except Exception:
                pass
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create User")
            try:
                usser = file.getvalue().strip()
            except Exception:
                pass
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create State")
            try:
                t_state = file.getvalue().strip()
            except Exception:
                pass
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("create City")
            try:
                t_city = file.getvalue().strip()
            except Exception:
                pass
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all BaseModel")
            try:
                self.assertIn(base_m, file.getvalue())
            except Exception:
                pass
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all City")
            try:
                self.assertIn(t_city, file.getvalue())
            except Exception:
                pass
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all User")
            try:
                self.assertIn(usser, file.getvalue())
            except Exception:
                pass
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all State")
            try:
                self.assertIn(t_state, file.getvalue())
            except Exception:
                pass

    def test_create_command_with_kwargs(self):
        """Test create command with kwargs."""
        with patch("sys.stdout", new=StringIO()) as file:
            starrrt = (f'create Place city_id="0001" name="My_house"')
            self.HBNB.onecmd(starrrt)
            t_place = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.HBNB.onecmd("all Place")
            try:
                t_vall = file.getvalue()
            except Exception:
                pass
            self.assertIn(t_place, t_vall)
            self.assertIn("'city_id': '0001'", t_vall)
            self.assertIn("'name': 'My house'", t_vall)

if __name__ == "__main__":
    unittest.main()
