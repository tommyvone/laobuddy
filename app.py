from flask import Flask, request, redirect, render_template, flash
from model import db, Member  




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

        # Check if email already exists
        existing_user = Member.query.filter_by(email=email,username=username).first()
        if existing_user:
            flash('Email already registered and username. Please log in or use a different email and username.')
            return render_template('signup.html')

    member = Member(
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

