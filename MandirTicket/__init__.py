import flask
import urllib
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=DESKTOP-KEO3N1T\SQLEXPRESS;DATABASE=AssetsDB")
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc:///?odbc_connect=%s" % params

db = SQLAlchemy(app)
db_main_user = db.Table('User', db.metadata, autoload=True, autoload_with=db.engine)

import MandirTicket.routes