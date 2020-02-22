from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
	'user' : 'Mizan',
	'datecreated' : '22/02/2020',
	'imageurl': 'https://lh3.googleusercontent.com/proxy/O0aadLhyI7re4rhuXHWb8e_nvPQ6GSyTArl-syQLeYIzXxAtOV7JvbbqnizV2AokLeikXrME6pPhi5N1qAWCxlSjQtqFjpWwgh5cGLv6Cum4k0vhXSyA4cAAlfj_F3kyNZCM',
	'title': 'Mitsubishi Evo 9 MR360',
	'cardescription' : 'Wynford Specialist Motors Have once again managed to get there hands on a stunning unmarked example of a Mitsubishi Lancer Evo FQ-300 Finished in Pamla red ,only 1 owner from new With only 11000 miles from new ,never seen the rain ,totally genuine just like when it left the factory,a real credit to its owner keeping it locked away indoors for Its 16 years ,This model is a genuine FQ-300 model with a FQ-330 upgrade from factory , also has the upgraded half leather recaro red & black Leather Seats,original bill of sale to hand, been serviced by Mitsubishi main dealers, Trackstar Tracker Fitted along with Clifford alarm ,2 Keys to hand, you will not find a better condition evo',
	'mileage' : '200,000 miles',
	'location' : 'Manchester, Salford',
	'contact' : '07462516278'

	},
	{
	'user' : 'James Grant',
	'imageurl':'https://www.classicdriver.com/sites/default/files/styles/full_width_slider/public/article_images/porsche-turbo-13.jpg',
	'datecreated' : '2/02/2020',
	'title': 'Rare 911 Turbo',
	'cardescription' : '3 owners / 9985 miles / Full service history and 2 years Porsche Approved warranty / 3.8L - 560hp / White with Black leather interior / A vehicle which bears our Porsche Approved seal has been professionally prepared by our Porsche-trained Technicians using only Porsche Genuine Parts. Our commitment includes: Minimum 24 months Porsche Approved Warranty and Porsche Assistance* / Vehicle inspected in compliance with our 111-point checklist / All work performed by Porsche-trained Technicians using Porsche Genuine Parts / Routine servicing/maintenance due within three months or 3,000 miles carried out / Minimum of 12 months MOT** / Fitment of N-rated tyres to minimum tread depth of 3mm / Body refinishing to Porsche standards / Full valet and final quality inspection / Independently monitored and audited standards.',
	'mileage' : '20,000 miles',
	'location' : 'London, Ilford',
	'contact' : '07462222278'

	}

]


@app.route("/home")
@app.route("/")
def home():
	return render_template('home.html', posts = posts, title = 'Home')

@app.route("/about")
def about():
	return render_template('about.html', title = 'About Us')

@app.route("/login")
def login():
	return render_template('login.html', title = 'Login')

@app.route("/register")
def register():
	return render_template('register.html', title = 'Register')


if __name__== '__main__':
	app.run(debug=True)

