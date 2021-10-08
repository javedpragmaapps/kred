#!/usr/bin/env python

"""Tests for `kred` package."""


import unittest
from nose2.tools import params


class TestStringMethods(unittest.TestCase):

    @params("Pragmaapps", "Pragmaapps Technalogy", "iPragmatech name as Pragmaapps")
    def test_is_knight(self, value):
        assert value.startswith('Pragmaapps')

    # Returns True if the string is in upper case.
    @params("Pragmaapps", "pragmaapps", "PRAGMAAPPS")
    def test_upper(self, value):
        print('test_upper')
        print(value)
        expected = 'PRAGMAAPPS'
        self.assertEqual(value, expected)
