from flask import render_template, redirect, url_for, request, Response
from forms import FipsFinderForm, DataPortalForm
from fips_helpers import find_state_county_place_fips
from logging import debug
from wufoo_helpers import submit_form_to_wufoo
from portal_data_helpers import insert_data_portal_record, get_data_portals, get_data_portal_csv

from flask import Flask, Response

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

@app.route('/data-portals/new', methods = ['GET'])
def new():
  form = DataPortalForm(Field205="Looks Good!")
  return render_template('data_portals/new.html', title = 'Data Portal Hunt', form = form)

@app.route('/data-portals/create', methods = ['POST'])
def create():
  form = DataPortalForm(request.form)
  if form.validate():
    submit_form_to_wufoo(request.form)
    insert_data_portal_record(request.form)
    return redirect('/thanks')
  return render_template('data_portals/new.html', title = 'Data Portal Hunt', form = form)

@app.route('/thanks', methods = ['GET'])
def thanks():
  return render_template('data_portals/thanks.html', title = 'Thanks')

@app.route('/data-portals/index')
def data_portals_list():
  portal_dict = get_data_portals()
  return render_template('data_portals/index.html', title = 'Data Portals', portal_dict = portal_dict)

@app.route('/data-portals/entries.csv')
def data_portals_csv():
  return Response(get_data_portal_csv(), mimetype='text/csv')
  