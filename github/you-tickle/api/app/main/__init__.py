from flask import Blueprint

bp = Blueprint('main', __name__)

from api.app.main import routes 
