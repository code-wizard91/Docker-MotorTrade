from PIL import Image
import os
import secrets
from application.models import Users, Adverts
from application import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, abort
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, AdvertForm
from flask_login import login_user, current_user, logout_user, login_required



@app.route("/home")
@app.route("/")
def home():
        posts = Adverts.query.all()
        return render_template('home.html',posts = posts, title = 'Home')

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

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profileimage', picture_fn)
    form_picture.save(picture_path)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def save_car_image(form_image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = random_hex + f_ext
    image_path = os.path.join(app.root_path, 'static/carimages', image_fn)
    form_image.save(image_path)

    return image_fn


@app.route("/account", methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.profile_image= picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        db.session.commit()
        flash('Your account has been updated','success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
    image_file = url_for('static',filename = 'profileimage/' + current_user.profile_image)
    return render_template('account.html', title='Account',image_file=image_file, form=form)


@app.route("/advert/new", methods=['GET','POST'])
@login_required
def new_advert():
    form = AdvertForm()
    if form.validate_on_submit():
        if form.image.data:
            image_file = save_car_image(form.image.data)
            advert = Adverts(user_id=current_user.user_id,car_title=form.title.data, car_descr=form.car_descr.data, price=form.price.data, mileage = form.mileage.data, location = form.location.data, contact_no=form.contact_no.data, image = image_file)
            db.session.add(advert)
            db.session.commit()
            flash('Your Advert Has Been Created! ','success')
            return redirect(url_for('home'))
        else:
            flash('Please Upload an Image','danger')
    return render_template('create_advert.html', title='New Advert',form=form, legend = 'New Advert')

@app.route("/advert/<int:adv_id>")
def advert(adv_id):
    advert = Adverts.query.get_or_404(adv_id)
    return render_template('advert.html', title=advert.car_title, post=advert)

@app.route("/advert/<int:adv_id>/update", methods=['GET','POST'])
@login_required
def update_advert(adv_id):
    advert = Adverts.query.get_or_404(adv_id)
    if advert.author != current_user:
        abort(403)
    form = AdvertForm()
    if form.validate_on_submit():
        if form.image.data:
            image_file = save_car_image(form.image.data)
            advert.image = image_file
        advert.car_title = form.title.data
        advert.car_descr = form.car_descr.data
        advert.price = form.price.data
        advert.mileage = form.mileage.data
        advert.location = form.location.data
        advert.contact_no = form.contact_no.data
        db.session.commit()
        flash('Your Advert Has Been Updated! ','success')
        return redirect(url_for('advert',adv_id=advert.adv_id))
    elif request.method == 'GET':
        form.title.data = advert.car_title
        form.car_descr.data = advert.car_descr
        form.price.data = advert.price
        form.mileage.data = advert.mileage
        form.location.data = advert.location
        form.contact_no.data = advert.contact_no
        form.image.data = advert.image
    return render_template('create_advert.html', title='Update Advert',form=form, legend = 'Update Advert')

@app.route("/advert/<int:adv_id>/delete", methods=['POST'])
@login_required
def delete_advert(adv_id):
    advert = Adverts.query.get_or_404(adv_id)
    if advert.author != current_user:
        abort(403)
    db.session.delete(advert)
    db.session.commit()
    flash('Your Advert Has Been Deleted ','success')
    return redirect(url_for('home'))
