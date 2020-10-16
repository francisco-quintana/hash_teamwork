
# Flask
from flask import render_template, redirect, url_for, flash
from flask_pymongo import pymongo

# Local config
from app import create_app
from app.form import SignInForm, SignUpForm
import dbconfig
import keys
import hash

# se crea la aplicación de flask
app = create_app()

#se le designa el nombre a la ruta seguido de los metodos que va a utilizar
@app.route('/', methods=['GET','POST'])
def signin():
    #se declara una variable con la instacia del formulario
    data_form = SignInForm()
    #variables que se usan en la página
    context = {
        'title':'Sign In',
        'data_form': data_form
    }
    #si se hace submit se ejecuta el siguiente código
    if data_form.validate_on_submit():
        #jala los dos campos ingresados por el usuario
        username= data_form.username.data
        password = data_form.password.data
        #se busca que el usuario exista en la base de datos
        user = dbconfig.db_users.users.find_one({'username':username})
        #hash de la pswd
        hs = hash.hashear(password)
        #si el usuario existe se ejecuta el siguiente codigo
        if user:
            #si la contraseña en la base de datos es igual a el hash ingresado
            if user['password'] == hs:
                #redireccion a la página de success
                return redirect('/success')
            else:
                #mensaje para el usuario
                flash('Incorrect Password')
        #mensaje para el usuario
        else:
            flash('User does not exist')
    #template que se va usar y variables que va a usar
    return render_template('signin.html', **context)

@app.route('/signup', methods=['GET','POST'])
def signup():
    #se declara una variable con la instacia del formulario
    data_form = SignUpForm()
    #variables que se usan en la página
    context={
        'title':'Sign Up',
        'data_form': data_form,
    }
    #si el usuario le da submit
    if data_form.validate_on_submit():
        #jala todos los datos ingresados por el usuario
        username = data_form.username.data
        email = data_form.email.data
        name = data_form.name.data
        password = data_form.password.data
        c_password = data_form.retry_password.data

        #si las dos contraseñas ingresadas por el usuario son iguales
        if password == c_password:
            #hash de la contraseña que ingreso el usuario
            password=hash.hashear(password)
            #se insertan los datos del usuario en la bd
            dbconfig.db_users.users.insert_one({
                'username': username,
                'email': email,
                'name' : name,
                'password' : password,
            })
            #redireccion al sign in
            return redirect('/')
        else:
            flash('Passwords do not match')

    return render_template('signup.html', **context)


@app.route('/success')
def success():
    #se crean llaves publicas y privadas RSA
    public_key=keys.public_key
    private_key=keys.private_key
    #se le pasan las variables creadas a el template
    return render_template('success.html',pukey=public_key,prkey=private_key)
