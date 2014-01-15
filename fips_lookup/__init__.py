from flask import Flask

app = Flask(__name__)
app.secret_key = 'EWOUB'

from fips_lookup import views

