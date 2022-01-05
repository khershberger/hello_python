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
        self.assertFalse(not(hello.return_true()))

class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.c = hello.HelloClass()
        cls.is_class_setup = True

    def setUp(self):
        print("setUp")
        self.c.set_count(5)
        self.is_setup = True
        
    def test_class(self):
        self.assertTrue(self.is_class_setup)
        self.assertTrue(self.is_setup)
        self.assertEqual(self.c.get_count(), 5)
        self.c.increment()
        self.assertEqual(self.c.get_count(), 6)
        
    def test_two(self):
        self.assertEqual(self.c.get_count(), 5)

    def tearDown(self):
        print("tearDown")
    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

if __name__ == '__main__':
    unittest.main()