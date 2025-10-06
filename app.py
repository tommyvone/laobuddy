from flask import Flask, request, redirect, render_template, flash
from model import db, Sember  
from sqlalchemy import func




app = Flask(__name__)
app.secret_key = 's3cr3t_k3y_987654321'


#PostgreSQL connection strin
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://laobuddy:Lisa243414133@localhost/laobuddy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize SQLAlchemy with app
db.init_app(app)



@app.route('/')
def home():
    return render_template('home.html')



@app.route('/profile')
def profile():
    return render_template('profile.html')



@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/signup', methods=['GET'])
def show_signup_form():
    return render_template('signup.html')
    


@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']

        # Check if email, username already exists
        existing_users = Sember.query.filter((Sember.email == email)).first()
        existing_username = Sember.query.filter((Sember.username == username)).first()
        if existing_users:
            flash('Email already exists')
            return render_template('signup.html')
        elif existing_username:
            flash('username alreay exists')
            return render_template('signup.html')

     

    member = Sember(
        first_name=request.form.get('firstName'),
        last_name=request.form.get('lastName'),
        username=request.form.get('username'),
        email=request.form.get('email'),
        password=request.form.get('password'),
        gender=request.form.get('gender'),
        country=request.form.get('country'),
        city=request.form.get('city')
    )
   
    db.session.add(member)
    db.session.commit()
    return render_template('success.html')

