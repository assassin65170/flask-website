from website import app
from flask import render_template, redirect, url_for, flash,request
from website.forms import Form, Login, Signup
from website import db
from website.models import Contact, Users
from website import bcrypt
from flask_login import login_user, logout_user, login_required, current_user



@app.route("/", methods=['GET', 'POST'])
def login():
    form = Login()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(email_address=form.email_address.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('home'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route("/signup/", methods=['GET','POST'])
def signup():
    form = Signup()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = Users(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    if form.errors != {}: 
        for err_msg in form.errors.values():
            flash(f'Error: {err_msg}', category='danger')
    return render_template('signup.html', form=form)

@app.route("/home/")
@login_required
def home():
    return render_template('home.html')


@app.route("/about/")
@login_required
def about():
    return render_template('about.html')


@app.route("/contact/", methods=['GET', 'POST'])
@login_required
def contact():
    form = Form()
    if form.validate_on_submit():
        contact = Contact(username=form.username.data,
                              email_address=form.email_address.data,
                              subject=form.subject.data,
                              message=form.message.data)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('contact'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error: {err_msg}', category='danger')
    return render_template('contact.html', form=form)



@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('login'))

