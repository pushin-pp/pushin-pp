from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password1")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category = "success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password. Try again.", category = "error")
        else:
            flash("Entered email is not associated with an existing account.", category = "error")

    return render_template("login.html", user = current_user)

@auth.route("/logout", methods = ["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign-up", methods = ["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        passwordConfirm = request.form.get("password2")
        schoolYear = request.form.get("schoolYear")
        # print(passwordConfirm)

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email is already associated to an account.", category = "error")
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category = "error")
        elif len(firstName) < 2:
            flash("First name must be greater than 2 characters.", category = "error")
        elif password1 != passwordConfirm:
            flash("Passwords don\'t match.", category = "error")
        elif len(password1) < 7:
            flash("Password must be greater than 7 characters.", category = "error")
        else:
            #add to database
            new_user = User(email=email, first_name=firstName, school_year = schoolYear, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created.", category = "success")

            return redirect(url_for("views.home"))
    return render_template("sign_up.html", user = current_user)


