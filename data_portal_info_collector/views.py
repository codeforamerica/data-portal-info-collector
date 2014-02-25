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

@app.route('/new', methods = ['GET'])
def new():
  form = DataPortalForm(Field205="Looks Good!")
  return render_template('data_portals/new.html', title = 'Data Portal Hunt', form = form)

@app.route('/create', methods = ['POST'])
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
  ordered_portal_dict = get_data_portals()
  return render_template('data_portals/index.html', title = 'Data Portals', ordered_portal_dict = ordered_portal_dict)

@app.route('/data-portals/entries.csv')
def data_portals_csv():
  return Response(get_data_portal_csv(), mimetype='text/csv')

@app.context_processor
def utility_processor():
  def string_to_list(items_string):
    return items_string.split(',')
  def truncate_url(url):
    return (url[:22] + '..') if len(url) > 22 else url
  return dict(string_to_list=string_to_list, truncate_url=truncate_url)
  