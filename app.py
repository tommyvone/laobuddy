from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#PostgreSQL connection strin
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://laobuddy:Lisa243414133@localhost/laobuddy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup',methods= ['GET','POST'])
def signup():
    return render_template('signup.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login')
def login():
    return render_template('login.html')



