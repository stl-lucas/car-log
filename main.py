from app import app, session, request, redirect, render_template, session, flash
from models import db, User, Car  

def get_current_carlist(owner):
    return Car.query.filter_by(owner=owner).all()

# User Login Controller
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = User.query.filter_by(email=email)
        if users.count() == 1:
            user = users.first()
            if password == user.password:
                session['user'] = user.email
                flash('welcome back, '+user.email)
                return redirect("/")
        flash('bad username or password')
        return redirect("/login")

# User registration controller
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']
        if not is_email(email):
            flash('zoiks! "' + email + '" does not seem like an email address')
            return redirect('/register')
        email_db_count = User.query.filter_by(email=email).count()
        if email_db_count > 0:
            flash('yikes! "' + email + '" is already taken and password reminders are not implemented')
            return redirect('/register')
        if password != verify:
            flash('passwords did not match')
            return redirect('/register')
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        session['user'] = user.email
        return redirect("/")
    else:
        return render_template('register.html')

# Simple email format validation
def is_email(string):
    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present

# Logout controller
@app.route("/logout", methods=['POST'])
def logout():
    del session['user']
    return redirect("/")

# Add new vehicles
@app.route("/add", methods=['POST'])
def add_car():
    # look inside the request to figure out what the user typed
    new_car_name = request.form['new-car']

    # if the user typed nothing at all, redirect and tell them the error
    if (not new_car_name) or (new_car_name.strip() == ""):
        error = "Please specify the vehicle name you want to add."
        return redirect("/?error=" + error)

    owner = User.query.filter_by(email=session['user']).first()
    car = Car(new_car_name, owner)
    db.session.add(car)
    db.session.commit()
    return render_template('add-confirmation.html', car=car)

# Home Controller
@app.route("/")
def index():
    owner = User.query.filter_by(email=session['user']).first()
    encoded_error = request.args.get("error")
    return render_template('edit.html', carlist=get_current_carlist(owner), error=encoded_error and cgi.escape(encoded_error, quote=True))


# Force user to register or login before viewing other pages and data
endpoints_without_login = ['login', 'register']

@app.before_request
def require_login():
    if not ('user' in session or request.endpoint in endpoints_without_login):
        return redirect("/register")

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

if __name__ == "__main__":
    app.run()
