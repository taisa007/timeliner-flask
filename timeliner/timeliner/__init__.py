from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config.from_object('timeliner.config')

db = SQLAlchemy(app)

import timeliner.views
