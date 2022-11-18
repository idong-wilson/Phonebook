from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import RegistrationForm
from app.models import User


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Home')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, phone_number=form.phone_number.data, address=form.address.data)
        db.session.add(user)
        db.session.commit()
        flash(f"{form.first_name.data} {form.last_name.data}'s info created successfully!", category='success')
        return redirect(url_for('homepage'))
    return render_template('register.html', title='Register', form=form)

