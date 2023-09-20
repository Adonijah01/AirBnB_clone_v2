#!/usr/bin/python3
"""DBStorage unittests module"""
import unittest
import pycodestyle
from models.engine.db_storage import DBStorage
from models.engine import db_storage


class TestDBStorage(unittest.TestCase):
    """Tests for DBStorage"""

    def testPyStandard(self):
        """Check python rules adhearance"""
        pepRules = pycodestyle.StyleGuide(quiet=True)
        check = pepRules.check_files(['models/engine/db_storage.py'])
        self.assertEqual(
            check.total_errors,
            0,
            'Found code style errors (and warnings).'
        )

    def testPyStandardForTest(self):
        """Check python rules adhearance"""
        pepRules = pycodestyle.StyleGuide(quiet=True)
        s = 'tests/test_models/test_engine/test_db_storage.py'
        check = pepRules.check_files([s])
        self.assertEqual(
            check.total_errors,
            0,
            'Found code style errors (and warnings).'
        )

    def testModuleDocs(self):
        """Check for module docs"""
        self.assertTrue(len(db_storage.__doc__) >= 1)

    def testClassDocs(self):
        """Check for class docs"""
        self.assertTrue(len(DBStorage.__doc__) >= 1)
