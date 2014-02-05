from flask import render_template, redirect, url_for, request
from forms import FipsFinderForm, DataPortalForm
from fips_helpers import find_state_county_place_fips
from logging import debug
from wufoo_helpers import submit_form_to_wufoo

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

@app.route('/new', methods = ['GET'])
def new():
  form = DataPortalForm(Field205="Looks Good!")
  return render_template('new.html', title = 'Data Portal Hunt', form = form)

@app.route('/create', methods = ['POST'])
def create():
  form = DataPortalForm(request.form)
  if form.validate():
    submit_form_to_wufoo(request.form)
    return redirect('/thanks')
  return render_template('new.html', title = 'Data Portal Hunt', form = form)

@app.route('/thanks', methods = ['GET'])
def thanks():
  return render_template('thanks.html', title = 'thanks')
