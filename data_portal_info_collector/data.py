from os.path import dirname, join
from csv import DictReader

states_path = join(dirname(__file__), 'lib/states.csv')
states = list(DictReader(open(states_path), dialect='excel-tab'))

counties_path = join(dirname(__file__), 'lib/counties.csv')
counties = list(DictReader(open(counties_path), dialect='excel-tab'))

places_path = join(dirname(__file__), 'lib/places.csv')
places = list(DictReader(open(places_path), dialect='excel-tab'))
