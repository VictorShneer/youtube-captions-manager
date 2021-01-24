from app.main import bp
from app.models import Task
from app.models import Token
from flask import render_template
import time
import requests
from flask import current_app


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/index')
def root():
    return current_app.send_static_file('index.html')

@bp.route('/api/time')
def current_time():
    return {'time':time.time()}

@bp.route('/api/tickle/<q>')
def tickle(q):
    r = requests.get(f'https://your-tickle-db.herokuapp.com/search_for_caption/?q={q}')
    # r = requests.get(f'http://127.0.0.1:5000/search_for_caption/?q={q}')
    return r.json()


