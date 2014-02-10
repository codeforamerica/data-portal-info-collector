import requests
from requests.auth import HTTPBasicAuth

def submit_form_to_wufoo(form_data):
  auth = HTTPBasicAuth('4OA6-OVIW-XEUE-FYQV', 'footastic')
  request_url = 'https://codeforamerica.wufoo.com/api/v3/forms/data-portal-hunt/entries.xml'
  data = form_data.to_dict()
  requests.post(url=request_url, data=data, auth=auth)