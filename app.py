from flask import Flask, session, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://car-log:password@localhost:3306/car-log'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)