
from flask import Flask, render_template, request, redirect, url_for, session

import sqlite3


## Initialize SQLite database
def init_db():
    print("vone bountham")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            birthday TEXT NOT NULL,
            gender TEXT NOT NULL,
            country TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

    init_db()






app = Flask(__name__)

# main route
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print('Received POST request')
        user_data = (
            request.form['firstName'],
            request.form['lastName'],
            request.form['username'],
            request.form['email'],
            request.form['birthday'],
            request.form['gender'],
            request.form['country'],
            request.form['city']
        )
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (
                    first_name, last_name, username, email,
                    birthday, gender, country, city
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', user_data)
            conn.commit()
            conn.close()
            return redirect(url_for('success'))
        except sqlite3.IntegrityError:
            return "Username already exists. Please choose another."

    return render_template('signup.html')

    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/success')
def success():
    return "Account created successfully! 🎉"







