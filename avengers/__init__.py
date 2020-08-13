from flask import Flask

from config import Config

#import for Flask DB and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from avengers import routes, models