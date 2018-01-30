from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    cars = db.relationship('Car', backref='owner')
    
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    make = db.Column(db.String(120))
    model = db.Column(db.String(120))
    year = db.Column(db.Integer)
    mileage = db.Column(db.Integer)
    sold = db.Column(db.Boolean)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    records = db.relationship('Record', backref='vehicle')

    def __init__(self, name, make, model, year, owner):
        self.name = name
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
        self.sold = False
        self.owner = owner

    def __repr__(self):
        return '<Car %r>' % self.name

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120))
    date = db.Column(db.String(120))
    note = db.Column(db.String(256))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('car.id'))

    def __init__(self, task, date, note, vehicle):
        self.task = task
        self.date = date
        self.note = note
        self.vehicle = vehicle

    def __repr__(self):
        return '<Record %r>' % self.task