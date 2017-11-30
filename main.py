from flask import Flask, request, redirect, render_template
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
    

    return render_template("sample.html", username='')

@app.route("/", methods=["POST"])
def index_post():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    #The user leaves any of the following fields empty: username, password, verify password.
    if (not username):# or (not password) or (not verify):
        username_error = "You must enter a username"

    username_error = is_valid_field(username, " ~^*") #checks for valid username
    password_error = is_valid_field(password, " ~^*") #checks for valid password
    
    #The user's password and password-confirmation do not match.
    if len(password) > 1 and password != verify:
        verify_error = "Password and verify password must match"

    #The user provides an email, but it's not a valid email.
    #valid email  has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
    if email:
        email_error = is_valid_email(email)

    if username_error or password_error or verify_error or email_error:
        if username_error:
            username = ""
        if password_error:
            password = ""
            verify = ""
        if email and email_error:
            email = ""
        return render_template("sample.html", username=username, password=password, verify=verify,email=email,
                                              username_error=username_error, password_error =  password_error,
                                              verify_error=verify_error, email_error=email_error)
    else:
        return redirect("/valid-signup?username={0}".format(username))

def is_valid_field(test_string, test_for):
    if len(test_string) < 3:
        return "This must be at least 3 characters long"
    if len(test_string) > 20:
        return "this can't be more than 20 characters long."

    for letter in test_string:
        if letter in test_for:
            return "This field cannot contain spaces or any of theese symbols '~^*"

    return ""

def is_valid_email (test_string):
    email_error = is_valid_field(test_string, " ~^")
    has_dot = False
    has_at = False

    if not email_error:
        for letter in test_string:
            if letter == ".":
                has_dot = True
            if letter == "@":
                has_at = True
        
    if has_dot and has_at:
        return ""
    else:
        return "Please make sure you email fits the pattern 'person@place.thing'"

@app.route("/valid-signup")
def valid_setup():
    username = request.args.get("username")
    return render_template("valid-signup.html", username=username)
app.run()