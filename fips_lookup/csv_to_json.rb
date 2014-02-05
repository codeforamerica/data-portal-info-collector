#!/usr/bin/env ruby

require 'csv'
require 'json'

places_array = []

state_hash = {}

CSV.foreach("lib/states.csv", { :col_sep => "\t" }) do |row|
  state_hash[row[2]] = row[8] if row[8] != "Name"
end

CSV.foreach("lib/counties.csv", { :col_sep => "\t" }) do |row|
  county_fips = "#{row[2]}#{row[4]}"
  places_array << "#{row[8]}, #{state_hash[row[2]]} (#{county_fips})" if row[8] != "Name"
end

CSV.foreach("lib/places.csv", { :col_sep => "\t" }) do |row|
  place_fips = "#{row[2]}#{row[3]}"
  places_array <<"#{row[8]}, #{state_hash[row[2]]} (#{place_fips})" if row[8] != "Name"
end

CSV.foreach("lib/states.csv", { :col_sep => "\t" }) do |row|
  places_array << "#{row[8]} (#{row[2]})" if row[8] != "Name"
end

File.open("static/places.js", "w") { |f| f.write(places_array.to_json
) }


