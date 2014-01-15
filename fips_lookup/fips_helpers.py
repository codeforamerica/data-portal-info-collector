
import data
import re

def find_state_county_place_fips(search_term):
  fips_matches = {}
  state_results = find_fips(data.states, search_term, "State FIPS")
  fips_matches['state'] = state_results

  county_results = find_fips(data.counties, search_term, "County FIPS")
  fips_matches['county'] = county_results

  place_results = find_fips(data.places, search_term, "Place FIPS")
  fips_matches['place'] = place_results
  return fips_matches

def find_fips(places_list, search_term, fips_key):
  results_list = [get_full_fips_code_and_place(row["Name"], row, fips_key)
                  for row in places_list
                  if re.match('(?i)' + search_term, row['Name'])]
  return results_list

def get_full_fips_code_and_place(place_name, row, fips_key):
  fips_code = row[fips_key]
  if fips_key != "State FIPS":
    fips_code = row["State FIPS"] + fips_code
    for state_row in data.states:
      if state_row['State FIPS'] == row["State FIPS"]:
        state_name = state_row["Name"]
        break
    place_name = place_name + ", " + state_name 
  return place_name + ": " + fips_code