from flask import Blueprint, render_template

home_views = Blueprint('home',__name__)

@home_views.route("/")
def home_user():
      
    return render_template('home/home_user.html')

@home_views.route("/cliente")
def home_cliente():
    return render_template('home/home_cliente.html')

@home_views.route("/admin")
def home_admin():
    return render_template("home/home_admin.html")