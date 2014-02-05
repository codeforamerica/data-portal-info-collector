from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, RadioField, TextAreaField, validators

class FipsFinderForm(Form):
  search_field = TextField(u'search', id="search_field")

class DataPortalForm(Form):
  Field1 = TextField(validators=[validators.Required(message=u'Please enter a place.')])
  Field2 = TextField(validators=[validators.Required(message=u'Please enter a URL.'), validators.URL()])

  Field4 = BooleanField()
  Field5 = BooleanField()
  Field6 = BooleanField()
  Field7 = BooleanField()
  Field8 = BooleanField()
  Field9 = BooleanField()
  Field10 = BooleanField()
  Field11 = BooleanField()
  Field12 = BooleanField()
  Field13 = BooleanField()
  Field14 = BooleanField()
  Field15 = BooleanField()

  Field105 = BooleanField()
  Field106 = BooleanField()
  Field107 = BooleanField()
  Field108 = BooleanField()

  Field209 = TextField()

  Field205 = RadioField(choices=[('Looks Good!','Looks Good!'),('Stuff seems missing.','Stuff seems missing.'),('This is a joke.','This is a joke.')], validators=[validators.Required(message=u'Please choose one.')])

  Field207 = TextAreaField()