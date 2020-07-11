from flask import (render_template, request, flash, redirect, url_for, jsonify)
from . import bp
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import RegistrationForm, LoginForm
from app.models import User


# Define all routes to application
@bp.route('/users/login', methods=['GET', 'POST'])
def login():
    print("Login Called")
    if current_user.is_authenticated:
        return redirect(url_for('bp.homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('bp.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('bp.homepage')
        return redirect(next_page)
    return render_template('account/login.html', title='Sign In', form=form)

# Get all registed users
@bp.route("/users")
def get_all_users():
    users = User.query.all()
    data = [user.serialize for user in users]

    return jsonify(data)

# Logout User
@bp.route('/users/logout')
def logout():
    logout_user()
    return redirect(url_for('bp.homepage'))

# Create a new User
@bp.route('/users/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('bp.homepage'))
    form = RegistrationForm()
    print(form.username.data)
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        print(user.username)
        user.set_password(form.password.data)
        User.insert(user)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('bp.login'))
    return render_template('account/register.html', title='Register', form=form)
