import unittest
from . import test_config

class JeliTestCase(unittest.TestCase):
    """ """
    def setUp(self):
        self.tc = test_config.JeliTestConfig()
        pass

    def test_jfs(self):
        self.assertTrue(
            self.tc.jeli_fs_test())

    def test_jfl(self):
        self.tc.jeli_file_loader()

    def test_jeaf(self):
        self.tc.jeli_eaf_processor()

    def test_jeli_stats(self):
        self.tc.jeli_stats()

    def test_jeli_exporter(self):
       self.tc.jeli_exporter()
       pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
