# Import necessary modules from Flask and SQLAlchemy
from flask import Flask, request, redirect, render_template, flash, session
from model import db, member  # Import database instance and user model
from sqlalchemy import func  # Optional: useful for aggregate queries

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 's3cr3t_k3y_987654321'  # Secret key for session management and flash messages

# Configure PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://laobuddy:Lisa243414133@localhost/laobuddy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind SQLAlchemy to the Flask app
db.init_app(app)

# Route for home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for user profile page
@app.route('/profile')
def profile():
    user_id = session.get('user_id')  # Get logged-in user's ID from session
    if not user_id:
        flash('Please log in first')  # Show message if not logged in
        return redirect('/login')  # Redirect to login page
    
    user = member.query.get(user_id)  # Fetch user from database
    return render_template('profile.html', user=user)  # Render profile with user data

# Route to log out the user
@app.route('/logout')
def logout():
    session.clear()  # Remove all session data
    flash('You have been logged out.')  # Show logout message
    return redirect('/login')  # Redirect to login page


# Route for login page and login logic
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        # Get login credentials from form
        identifier = request.form.get('emailOrUsername')
        password = request.form.get('password')

        # Find user by email or username
        user = member.query.filter(
            (member.email == identifier) | (member.username == identifier)
        ).first()

        # Check if user exists and password matches
        if user and user.password == password:
            session['user_id'] = user.id  # Store user ID in session
            return redirect('/profile')  # Redirect to profile page
        else:
            flash('Wrong password or email Please check')  # Show error message
            return render_template('login.html')  # Reload login page
    else:
        return render_template('login.html')  # Show login form on GET request




# Route to show signup form
@app.route('/signup', methods=['GET'])
def show_signup_form():
    return render_template('signup.html')

# Route to handle signup form submission
@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        # Get email and username from form
        email = request.form['email']
        username = request.form['username']

        # Check if email or username already exists
        existing_users = member.query.filter(member.email == email).first()
        existing_username = member.query.filter(member.username == username).first()
        if existing_users:
            flash('Email already exists')  # Show error if email is taken
            return render_template('signup.html')
        elif existing_username:
            flash('username already exists')  # Show error if username is taken
            return render_template('signup.html')

    # Create new user with form info
    member = member(
        first_name=request.form.get('firstName'),
        last_name=request.form.get('lastName'),
        username=request.form.get('username'),
        email=request.form.get('email'),
        password=request.form.get('password'),  # Note: should be hashed in production
        gender=request.form.get('gender'),
        country=request.form.get('country'),
        city=request.form.get('city')
    )
   
    db.session.add(member)  # Add new user to database
    db.session.commit()  # Save changes
    return render_template('success.html')  # Show success page after signup
