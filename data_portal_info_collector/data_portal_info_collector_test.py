"""
    Data Portal Info Collector Tests
    ~~~~~~~~~~~~
"""
import os
from views import app
import unittest
import tempfile
from db_connection_helpers import get_db_connection

class DataPortalInfoCollectorTestCase(unittest.TestCase):

  def setUp(self):

  def tearDown(self):
    os.close(self.db_fd)
    os.unlink(app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()