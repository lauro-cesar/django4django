import os 
import unittest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "___.settings")

from djangotoolbox.admin import APISiteAdmin 


class TestUtils(unittest.TestCase):
    def test_logger_exists(self):
        try:
            from djangotoolbox.utils import Logger as logger                       
        except Exception as e:
            self.fail()        
        self.assertIsNotNone(logger,"Logger exists") 


if __name__ == '__main__':
    unittest.main()
