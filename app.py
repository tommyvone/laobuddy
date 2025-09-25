from flask import Flask, render_template, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bountham:Lisa243414133@localhost/laobuddy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  

@app.route('/')
def home():
    return render_template('home.html')
from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bountham:Lisa243414133@localhost/laobuddy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    # Get form data
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')  # In production, hash this!
    gender = request.form.get('gender')
    country = request.form.get('country')
    city = request.form.get('city')

    # Create new user
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=password,
        gender=gender,
        country=country,
        city=city
    )

    # Insert into database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/profile.html')
def profile():
    users = User.query.all()
    return render_template('profile.html',users=users)
