from flask import Blueprint

bp = Blueprint('tasks', __name__)

from api.app.tasks import regular_upload
 
