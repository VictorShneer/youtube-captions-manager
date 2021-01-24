import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from redis import Redis
import rq

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../build', static_url_path = '/', template_folder='../build')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)

    # blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    # blueprint
    from app.tasks import bp as tasks_bp
    app.register_blueprint(tasks_bp)

    app.redis = Redis.from_url(app.config['REDISTOGO_URL'])
    app.task_queue = rq.Queue('tickle-tasks', connection=app.redis, default_timeout=1200)

    return app

from app import models
