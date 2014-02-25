from db_connection_helpers import get_db_connection
import re
import csv
import os
from time import gmtime, strftime
import io
from collections import OrderedDict

def insert_data_portal_record(form_data):
  conn = get_db_connection()
  cur = conn.cursor()
  state = get_state_from_place(form_data["Field1"])
  data_set_array = [form_data.get("Field" + str(x)) for x in range(4, 16)
                    if form_data.get("Field" + str(x)) is not None]
  data_sets = ', '.join(data_set_array)
  included_formats_array = [form_data.get("Field" + str(x)) for x in range(105, 109)
                    if form_data.get("Field" + str(x)) is not None]
  included_formats = ','.join(included_formats_array)
  cur.execute("""insert into data_portals (place, portal_url, data_sets, included_formats,
              press_release_url, data_completeness, comments, state, created_at) 
              values (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", \
              (form_data['Field1'], form_data["Field2"], data_sets,
               included_formats, form_data["Field209"], form_data["Field205"],
               form_data["Field207"], state, strftime('%Y-%m-%d %H:%M:%S', gmtime())))
  conn.commit()
  conn.close()

def get_state_from_place(place):
  state_fips = re.search('\d{2}', place).group(0)
  dir_root = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(dir_root, 'lib/states.csv')
  with open(filename, 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
      if row[2] == state_fips:
        return row[8]

def get_data_portal_csv():
  output = io.BytesIO()
  writer = csv.writer(output)
  csvdata = get_data_portals()
  writer.writerow(['id', 'place', 'portal url', 'data sets', 'included formats', 'press release url', 'data completeness', 'comments', 'state', 'created at'])
  for key, records in csvdata.iteritems():
    for record in records:
      writer.writerow(record)
  return output.getvalue()

def get_data_portals():
  conn = get_db_connection()
  cur = conn.cursor()
  select_statement = "select * from data_portals order by state, created_at"
  cur.execute(select_statement)
  data_portals = cur.fetchall()
  conn.close
  return get_data_portal_dict(data_portals)

def get_data_portal_dict(data_portals):
  portal_dict = {}
  for portal in data_portals:
    state = portal[8]
    if state in portal_dict:
      portal_dict[state].append(portal)
    else:
      portal_dict[state] = [portal]
  ordered_dict = OrderedDict(sorted(portal_dict.items(), key=lambda t: t[0]))
  return ordered_dict