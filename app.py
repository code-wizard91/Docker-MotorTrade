from flask import Flask, render_template
app = Flask(__name__)

posts = [
	{
	'user' : 'Mizan',
	'datecreated' : '22/02/2020',
	'title': 'Advert Post 1',
	'cardescription' : 'First advert test content',
	'mileage' : '200,000 miles',
	'location' : 'Manchester, Salford',
	'contact' : '07462516278'

	},
	{
	'user' : 'James Grant',
	'datecreated' : '2/02/2020',
	'title': 'Advert Post 2',
	'cardescription' : 'second test content',
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

