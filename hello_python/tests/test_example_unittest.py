# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 08:58:03 2022

@author: kyleh
"""

import unittest

import hello

class TestStuff(unittest.TestCase):
    def test_return_true(self):
        self.assertTrue(hello.return_true())

    def test_assert_false(self):
        self.assertFalse(hello.return_true())

if __name__ == '__main__':
    unittest.main()