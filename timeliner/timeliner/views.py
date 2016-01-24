from flask import request, render_template, redirect
from flask.helpers import url_for, flash
from timeliner import app, db
from timeliner.models import User


@app.route('/')
def index():
    data = 'hello'
    return render_template('index.html', data=data)


@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('user_list.html', users=users)


@app.route('/users/new')
def new_user():
    return render_template('new_user.html')


@app.route('/users/add', methods=['POST'])
def add_user():
    user = User(
        name=request.form['name'],
        password=request.form['password'],
        email=request.form['password'],
    )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('show_users'))


@app.route('/users/<int:user_id>/')
def edit_user():
    return render_template('edit_user.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def post_login():
    username = request.form['username']
    flash('You were logged in')
    return redirect(url_for('index'))

