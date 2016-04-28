import requests
import json

url = 'http://stash.compjour.org/samples/cpsc/recalls201604.json'

def get_data():
    resp = requests.get(url)
    txt = resp.text
    data = json.loads(txt)
    return data