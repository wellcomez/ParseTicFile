from futuhist import *
import unittest  # The test framework


class test(unittest.TestCase):
    def test_get_stock_list(self):
        get_stock_list()

    def test_build_kdata_index(self):
        ret = build_kdata_index()
        print(ret)
