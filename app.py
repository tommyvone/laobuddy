from flask import Flask, render_template
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bountham:Lisa243414133@localhost/laobuddy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # ✅ This links your app to the db instance


@app.route('/profile.html')
def show_users():
    with app.app_context():
        users = User.query.all()
        return render_template('profile.html', users=users)
