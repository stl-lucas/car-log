from flask import Flask, session, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tllucas1_car-log:SXJ#Rs]ATabL@localhost:3306/tllucas1_car-log'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)