# TODO Mentors: Explain the concept of a web server & routes

from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome_to_my_website():
        data = "Welcome to my website!"
        return data

# TODO Exercise: add a page called 'about' which shows your name & your city

