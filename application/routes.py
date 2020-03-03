from application.models import Users, Adverts
from application import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from application.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

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
        if current_user.is_authenticated:
            flash('You are Logged in','danger')
            return redirect(url_for('home'))
        form = LoginForm()
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                flash('Login Successful','success')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Login Unsuccessful, Please check login details','danger')
        return render_template('login.html', title = 'Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
        if current_user.is_authenticated:
            flash('You are Logged in','danger')
            return redirect(url_for('home'))
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = Users(username= form.username.data , first_name= form.first_name.data, last_name= form.last_name.data ,email = form.email.data ,password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('You have successfully created an account! You can now login','success')
            return redirect(url_for('login'))
        return render_template('register.html', title = 'Register', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    image_file = url_for('static',filename = 'profileimage/' + current_user.profile_image)
    return render_template('account.html', title = 'Account',image_file = image_file)
