from flask import Flask
from flask import render_template
from jinja2 import Environment
from get_data import get_data

app = Flask(__name__)
recalls_data = get_data()

def date_format(date_in):
	return date_in[:10]

def injury(inj):
	if len(inj) > 0:
		return True
	return False

app.jinja_env.filters['date_format'] = date_format
app.jinja_env.tests['injury'] = injury

@app.route("/")
def homepage():
	html = render_template('homepage.html',
		                   recalls=recalls_data,
		                   recalls_count=len(recalls_data))
	return html

if __name__ == '__main__':
	app.run(use_reloader=True, debug=True)