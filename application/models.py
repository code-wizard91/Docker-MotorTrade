from datetime import datetime
from application import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    #adv_id = db.Column(db.Integer, db.ForeignKey('adverts.adv_id'), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    adverts = db.relationship('Adverts', backref='author', lazy=True)

    def __repr__(self):
        return f"Users'{self.username}','{self.email}','{self.profile_image}')"


class Adverts(db.Model):
    adv_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    car_title = db.Column(db.String(100), nullable=False)
    car_descr = db.Column(db.Text, nullable=False)
    price = db.Column(db.String(150), nullable=False)
    mileage = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(300), nullable=False)
    contact_no = db.Column(db.String(15), nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    date_adv = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Adverts('{self.adv_id}','{self.car_title}','{self.image}','{self.date_adv}')"
