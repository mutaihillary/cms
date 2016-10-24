from flask import Flask, render_template, flash, request, url_for, redirect ,session
from wtforms.validators import DataRequired,Length, EqualTo, Email, Regexp
from wtforms import Form, BooleanField, SubmitField, PasswordField, StringField, ValidationError, TextAreaField
from flask_login import login_required
from content_management import Content
from functools import wraps
from dbconnect import connection
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc


TOPIC_DICT = Content()

app = Flask(__name__)

"""""
class RegistrationForm(Form):
    username = StringField('Username',validators=[DataRequired(),Length(4, 20)])
    email = StringField('Email Address',validators=[DataRequired(),Length(6,50),
                                                    Email()])

    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')])
    Confirm = PasswordField('Repeat password ', validators=[DataRequired()])
    submit = SubmitField('Register')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 02, 2016)',
                              validators=[DataRequired()])"""""


class RegistrationForm(Form):
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                              'Usernames must have only letters, '
                                              'numbers, dots or underscores')])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('confirm', message='Passwords must match.')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)',
                              validators=[DataRequired()])


@app.route('/register/', methods=["GET", "POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = connection()

            x = c.execute("SELECT * FROM users WHERE username = (%s)",
                          (thwart(username)))

            if int(x) > 0:
                flash("That username is already taken, please choose another")
                return render_template('register.html', form=form)

            else:
                c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
                          (thwart(username), thwart(password), thwart(email),
                           thwart("/introduction-to-python-programming/")))

                conn.commit()
                flash("Thanks for registering!")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('dashboard'))

        return render_template("register.html", form=form)

    except Exception as e:
        return (str(e))

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login_page'))

    return wrap


@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    gc.collect()
    return redirect(url_for('dashboard'))


@app.route('/login/', methods=["GET", "POST"])
def login_page():
    error = ''
    try:
        c, conn = connection()
        if request.method == "POST":

            data = c.execute("SELECT * FROM users WHERE username = (%s)",
                             thwart(request.form['username']))

            data = c.fetchone()[2]

            if sha256_crypt.verify(request.form['password'], data):
                session['logged_in'] = True
                session['username'] = request.form['username']

                flash("You are now logged in")
                return redirect(url_for("dashboard"))

            else:
                error = "Invalid credentials, try again."

        gc.collect()

        return render_template("login.html", error=error)

    except Exception as e:
        # flash(e)
        error = "Invalid credentials, try again."
        return render_template("login.html", error=error)


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/dashboard/')
def dashboard():
    #flash("flash test!!!!")
    return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route(TOPIC_DICT["Basics"][0][1], methods=['GET', 'POST'])
def introduction_to_python_programming():
    update_user_tracking()
    completed_percentages = topic_completion_percent()
    return render_template("tutorials/basics/python-introduction.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Basics"][0][1], curTitle=TOPIC_DICT["Basic"][0][1],  nextLink = TOPIC_DICT["Basics"][1][1], nextTitle = TOPIC_DICT["Basics"][1][1])


@app.route(TOPIC_DICT["Basics"][1][1], methods=['GET', 'POST'])
def python_tutorial_print_function_strings():
    update_user_tracking()
    completed_percentages = topic_completion_percent()
    return render_template("tutorials/basics/print-function-and-strings.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Basics"][1][1], curTitle=TOPIC_DICT["Basic"][1][1],  nextLink = TOPIC_DICT["Basics"][2][1], nextTitle = TOPIC_DICT["Basics"][2][1])


@app.route(TOPIC_DICT["Basics"][2][1], methods=['GET', 'POST'])
def math_basics_python_3_beginner_tutorial():
    update_user_tracking()
    completed_percentages = topic_completion_percent()
    return render_template("tutorials/basics/math-with-python.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Basics"][2][1], curTitle=TOPIC_DICT["Basic"][2][1],  nextLink = TOPIC_DICT["Basics"][3][1], nextTitle = TOPIC_DICT["Basics"][3][1])

@app.route(TOPIC_DICT["Basics"][3][1], methods=['GET', 'POST'])
def python_3_variables_tutorial():
    update_user_tracking()
    completed_percentages = topic_completion_percent()
    return render_template("tutorials/basics/variables.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Basics"][3][1], curTitle=TOPIC_DICT["Basic"][3][1],  nextLink = TOPIC_DICT["Basics"][4][1], nextTitle = TOPIC_DICT["Basics"][4][1])

@app.route(TOPIC_DICT["Basics"][4][1], methods=['GET', 'POST'])
def python_3_loop_tutorial():
    update_user_tracking()
    completed_percentages = topic_completion_percent()
    return render_template("tutorials/basics/while-loop.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Basics"][4][1], curTitle=TOPIC_DICT["Basic"][4][1],  nextLink = TOPIC_DICT["Basics"][5][1], nextTitle = TOPIC_DICT["Basics"][5][1])




if __name__ == "__main__":
    app.config['SESSION_TYPE'] = 'memcached'
    app.config['SECRET_KEY'] = 'super secret key'

    app.run(debug=True)