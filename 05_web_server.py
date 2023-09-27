# TODO Mentors: Explain the concept of a web server & routes

"""
Reads:
    What is a web server? https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server
    What is Flask? https://pythonbasics.org/what-is-flask-python/
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome_to_my_website():
        data = "Welcome to my website!"
        return data

# TODO TechWomen Exercise 1:
#       1. Run your Flask API with the command `flask --app 05_web_server.py run --host=0.0.0.0`
#       2. Check your website from your browser


# TODO TechWomen Exercise 1:  Add a page called 'about' which shows your name & your city

