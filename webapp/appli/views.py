from flask import Blueprint, render_template

appli = Blueprint("appli", __name__, template_folder="templates")

@appli.route("/")
def index():
    return render_template("appli/index.html")


