from flask import Flask, request, redirect, render_template
from model import db, Member  




app = Flask(__name__)

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
    


@app.route('/signup', methods=['POST'])
def signup():
    
    username = request.form.get('username')
    email = request.form.get('email')

    # check if username or email already exists
    existin_user = Member.query.filter(
        (Member.username == username) | (Member.email == email)).first()
    if existin_user:
        error = "Username or email already exists. Please choose another."
        return render_template('signup.html',error=error)

    # Proceed with creating the new membeer
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
    except Exception as e:
        db.session.rollback()
        print("Error:", e)
        return render_template('signup.html', error="Something went wrong.")


