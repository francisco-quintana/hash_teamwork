#set FLASK_APP=main.py
#set FLASK_DEBUG=1
# FLASK_ENV=development

# Flask
from flask import render_template, redirect, url_for, flash
from flask_pymongo import pymongo

# Local config
from app import create_app
from app.form import SignInForm, SignUpForm
import dbconfig
import keys
import hash

app = create_app()


@app.route('/', methods=['GET','POST'])
def signin():
    data_form = SignInForm()
    context = {
        'title':'Sign In',
        'data_form': data_form
    }
    if data_form.validate_on_submit():
        username= data_form.username.data
        password = data_form.password.data

        user = dbconfig.db_users.users.find_one({'username':username})
        hs = hash.hashear(password)

        if user['password'] == hs:
            return redirect('/success')
        else:
           flash('Incorrect Password')

    return render_template('signin.html', **context)

@app.route('/signup', methods=['GET','POST'])
def signup():
    data_form = SignUpForm()
    context={
        'title':'Sign Up',
        'data_form': data_form,
    }

    if data_form.validate_on_submit():
        username = data_form.username.data
        email = data_form.email.data
        name = data_form.name.data
        password = data_form.password.data
        c_password = data_form.retry_password.data

        if password == c_password:
            password=hash.hashear(password)
            dbconfig.db_users.users.insert_one({
                'username': username,
                'email': email,
                'name' : name,
                'password' : password,
            })
            return redirect('/')
        else:
            flash('Passwords do not match')

    return render_template('signup.html', **context)


@app.route('/success')
def success():
    public_key=keys.public_key
    private_key=keys.private_key
    return render_template('success.html',pukey=public_key,prkey=private_key)
