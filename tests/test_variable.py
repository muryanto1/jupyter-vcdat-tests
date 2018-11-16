import unittest
import os 
import sys
import time

this_dir = os.path.abspath(os.path.dirname(__file__))
lib_dir = os.path.join(this_dir, '..', 'lib')
sys.path.append(lib_dir)

#print("xxx xxx lib_dir: {d}".format(d=lib_dir))

# from BaseTestCase import BaseTestCase
from BaseTestCase import BaseTestCase
from BasePage import InvalidPageException
from MainPage import MainPage

class BrowserTest(BaseTestCase):
    def test_vcdat_jupyter_lab(self):
        print("xxx test_vcdat_jupyter_lab xxx")
        ws = "http://localhost:8888/?token=fafc834780204f1b82de8c0aca97b9cdb52ae76b21f60b45"
        #ws = "www.google.com"
        main_page = MainPage(self.driver, ws)

        main_page.load_file("clt.nc")


if __name__ == '__main__':
    unittest.main(verbosity=2)
