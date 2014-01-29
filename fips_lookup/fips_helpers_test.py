import os
from fips_helpers import find_state_county_place_fips
import unittest

class FipsHelpersTestCase(unittest.TestCase):

  def test_find_state_county_place_fips(self):
    """given a search term, returns the matching fips codes for a state, county, state"""
    fips_codes = find_state_county_place_fips("denver")
    self.assertEqual(fips_codes['state'],[])
    self.assertIn('Denver County, Colorado: 08031', fips_codes['county'])
    self.assertIn('Denver town, Indiana: 1817776', fips_codes['place'])

if __name__ == '__main__':
  unittest.main()
