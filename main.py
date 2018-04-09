from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    verpass = request.form['verify-password']
    email = request.form['email']

    name_error = None
    password_error = None
    verify_error = None
    email_error = None
    
    if (len(username) < 3) or (len(username) > 20) or (username != username.strip(' ')):
        name_error = "Username must be between 3 and 20 characters and cannot contain spaces"
        
    if (len(password) < 3) or (len(password) > 20) or (password != password.strip(' ')):
        password_error = "Password must be between 3 and 20 characters and cannot contain spaces"

    if password != verpass:
        verify_error = "Passwords do not match"

    if email and ((email.count('@') != 1) or (email.count('.') != 1) or (email.count(' ') != 0)):
        email_error = "Enter a valid email or leave this field blank"

    if name_error or password_error or verify_error or email_error:
        return render_template('signup.html', name_error=name_error, password_error=password_error, verify_error=verify_error, email_error=email_error, keepusername=username, keepemail=email)

    else:
        return render_template('welcome.html', username=username)

@app.route("/")
def index():
    return render_template('signup.html')

app.run()