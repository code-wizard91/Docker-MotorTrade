from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime



app = Flask(__name__)
app.config['SECRET_KEY'] = 'fee323f72238c94ce34302364eb0b21a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flaskapp'
db = SQLAlchemy(app)

class Users(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    adv_id = db.Column(db.Integer, db.ForeignKey('adverts.adv_id'), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    adverts = db.relationship('Adverts', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.profile_image}')"
		

class Adverts(db.Model):
    adv_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    car_title = db.Column(db.String(100), nullable=False)
    car_descr = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float(), nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(300), nullable=False)
    contact_no = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(300), nullable=False)
    date_adv = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Adverts('{self.adv_id}','{self.car_title}','{self.image}','{self.date_adv}')"
		





posts = [
	{
	'user' : 'Mizan',
	'datecreated' : '22/02/2020',
	'imageurl': 'https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/gallery_slide/public/496634680.jpg?itok=C0PDTs1E',
	'title': 'Mitsubishi Evo 9 MR360',
	'cardescription' : 'Wynford Specialist Motors Have once again managed to get there hands on a stunning unmarked example of a Mitsubishi Lancer Evo FQ-300 Finished in Pamla red ,only 1 owner from new With only 11000 miles from new ,never seen the rain ,totally genuine just like when it left the factory,a real credit to its owner keeping it locked away indoors for Its 16 years ,This model is a genuine FQ-300 model with a FQ-330 upgrade from factory , also has the upgraded half leather recaro red & black Leather Seats,original bill of sale to hand, been serviced by Mitsubishi main dealers, Trackstar Tracker Fitted along with Clifford alarm ,2 Keys to hand, you will not find a better condition evo',
	'mileage' : '200,000 miles',
	'location' : 'Manchester, Salford',
	'contact' : '07462516278',
	'price' : '£15,000'

	},
	{
	'user' : 'James Grant',
	'imageurl':'https://www.classicdriver.com/sites/default/files/styles/full_width_slider/public/article_images/porsche-turbo-13.jpg',
	'datecreated' : '2/02/2020',
	'title': 'Rare 911 Turbo',
	'cardescription' : '3 owners / 9985 miles / Full service history and 2 years Porsche Approved warranty / 3.8L - 560hp / White with Black leather interior / A vehicle which bears our Porsche Approved seal has been professionally prepared by our Porsche-trained Technicians using only Porsche Genuine Parts. Our commitment includes: Minimum 24 months Porsche Approved Warranty and Porsche Assistance* / Vehicle inspected in compliance with our 111-point checklist / All work performed by Porsche-trained Technicians using Porsche Genuine Parts / Routine servicing/maintenance due within three months or 3,000 miles carried out / Minimum of 12 months MOT** / Fitment of N-rated tyres to minimum tread depth of 3mm / Body refinishing to Porsche standards / Full valet and final quality inspection / Independently monitored and audited standards.',
	'mileage' : '20,000 miles',
	'location' : 'London, Ilford',
	'contact' : '07462222278',
	'price' : '£75,000'

	}

]


@app.route("/home")
@app.route("/")
def home():
	return render_template('home.html', posts = posts, title = 'Home')

@app.route("/about")
def about():
	return render_template('about.html', title = 'About Us')

@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful, Please check login details','danger')
	return render_template('login.html', title = 'Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account Created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form=form)




if __name__== '__main__':
	app.run(debug=True)

