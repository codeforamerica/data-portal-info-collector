from flask import render_template, redirect, url_for, request
from forms import FipsFinderForm
from fips_helpers import find_state_county_place_fips
from logging import debug

from flask import Flask

app = Flask(__name__)
app.secret_key = 'EWOUB'

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
  form = FipsFinderForm()
  return render_template('index.html', title = 'FIPS Lookup', form = form)

@app.route('/lookup', methods = ['GET'])
def lookup():
  fips_codes = find_state_county_place_fips(request.args.get('search_field'))

  form = FipsFinderForm()
  return render_template('index.html', title = 'FIPS Lookup',
                       form = form, state_fips = fips_codes['state'],
                       county_fips = fips_codes['county'],
                       place_fips = fips_codes['place'])
