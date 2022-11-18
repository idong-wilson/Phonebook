from phonebook_flask import app
from flask import render_template, url_for, redirect, flash
from phonebook_flask.forms import RegistrationForm


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Home')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f"{form.first_name.data} {form.last_name.data}'s info created successfully!")
        return redirect(url_for('homepage'))
    return render_template('register.html', title='Register', form=form)

