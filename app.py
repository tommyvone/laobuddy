
from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')