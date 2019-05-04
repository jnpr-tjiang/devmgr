#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_devmgr
----------------------------------

Tests for `devmgr` module.
"""

import unittest

import devmgr


class TestDevmgr(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(devmgr.__version__)

    def tearDown(self):
        pass
