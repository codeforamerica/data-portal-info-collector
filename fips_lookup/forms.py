from flask.ext.wtf import Form
from wtforms import TextField

class FipsFinderForm(Form):
  search_field = TextField(u'search', id="search_field")


