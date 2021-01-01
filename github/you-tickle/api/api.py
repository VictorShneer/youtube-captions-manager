from flask import Flask
import time

app = Flask(__name__)

@app.route('/time')
def current_time():
	return {'time':time.time()}