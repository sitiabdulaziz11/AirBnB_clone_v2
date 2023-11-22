#!/usr/bin/python3
"""
File that tests console codes
"""

import unittest
import pep8
import inspect
import console
HBNBCommand = console.HBNBCommand


class TestDoCreateMethod(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pep8_conformance_console(self):
        """
        Test console.py file conforms to PEP8.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """
        Test test/test_console.py conforms to PEP8.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """
        Test for the console.py module docstring
        """
        self.assertIsNot(
                console.__doc__, None,
                "console.py needs a docstring")

        self.assertTrue(len(
            console.__doc__) >= 1,
            "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """
        Test for the HBNBCommand class docstring
        """
        self.assertIsNot(
                HBNBCommand.__doc__, None,
                "HBNBCommand class needs a docstring")

        self.assertTrue(len(
            HBNBCommand.__doc__) >= 1,
            "HBNBCommand class needs a docstring")
