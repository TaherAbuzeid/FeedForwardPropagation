from flask import Flask
skills_app = Flask(__name__)


@skills_app.route("/")
def homepage():
    return "Hello From Flask Framework"

@skills_app.route("/about")
def about():
    return "About Page From Flask Framework"
