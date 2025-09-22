
from flask import Flask, render_template, request, redirect, session
import sqlite3
from Anyfunctions import

app = Flask(__name__)

# main route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET','POST'])
def signup():

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


# Create SQlite table for user
def init_db():
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXIST users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
            )
        ''')




















