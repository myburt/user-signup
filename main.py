from flask import Flask, request, redirect, render_template
import re
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader= jinja2.FileSystemLoader
(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    #if there is an error
    

    return render_template("sample.html")

@app.route("/", methods=["POST"])
def index_post():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_re = re.compile('\w-')

    #The user leaves any of the following fields empty: username, password, verify password.
    if (not username):# or (not password) or (not verify):
        username_error = "You must enter a username"
    elif not re.match(user_re, username):
        username_error = "Username is invalid please reenter"
        
    #The user's username or password is not valid -- for example, it contains a space character 
    # or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).

    #The user's password and password-confirmation do not match.

    #The user provides an email, but it's not a valid email.
    #valid email  has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
    return render_template("sample.html", username_error=username_error)

app.run()