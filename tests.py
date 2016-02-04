# -*- encoding: utf-8 -*-
#!/usr/bin/env python
from __future__ import absolute_import, print_function, unicode_literals

import datetime
import unittest

from nin import NinValidator

class TestDK(unittest.TestCase):
    def setUp(self):
        self.validator = NinValidator(country='dk')

    def test_sanitize(self):


        self.validator.nin = '123456-1234'
        self.assertEqual(self.validator.sanitize, '1234561234')

        self.validator.nin = '123456 1234'
        self.assertEqual(self.validator.sanitize, '1234561234')

        self.validator.nin = '123456--1234'
        self.assertEqual(self.validator.sanitize, '1234561234')

        self.validator.nin = 1234561234
        self.assertEqual(self.validator.sanitize, '1234561234')

        with self.assertRaises(TypeError):
            self.validator.nin = 'abc'
            self.validator.sanitize()

        with self.assertRaises(TypeError):
            self.validator.nin = '123456-123A'
            self.validator.sanitize()

        with self.assertRaises(TypeError):
            self.validator.nin = '123456+1234'
            self.validator.sanitize()

    def test_getage(self):
        diff = datetime.date.today().year - 1900
        self.validator.nin = '100600-1234'
        self.assertEqual(self.validator.age, diff)

        diff = datetime.date.today().year - 1981
        self.validator.nin = '100681-1234'
        self.assertEqual(self.validator.age, diff)

        diff = datetime.date.today().year - 1881
        self.validator.nin = '100681-5234'
        self.assertEqual(self.validator.age, diff)

        diff = datetime.date.today().year - 2000
        self.validator.nin = '100600-9234'
        self.assertEqual(self.validator.age, diff)

        diff = datetime.date.today().year - 2000
        self.validator.nin = '100600-5234'
        self.assertEqual(self.validator.age, diff)


if __name__ == '__main__':
    unittest.main()

