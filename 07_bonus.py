# TODO Mentors: Explain the requirements of the exercise

"""
Reads:
    How to print emoji: https://medium.com/analytics-vidhya/how-to-print-emojis-using-python-2e4f93443f7e
    Emoji list https://unicode.org/emoji/charts/emoji-list.html
"""

from flask import Flask, render_template
import requests
import os
import emoji

app = Flask(__name__, template_folder='template')

api_key = ""  # add your api key here
city = "Istanbul"
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}]&aqi=no'

response = requests.get(url)


# TODO TechWomen Last Exercise 1:
#  1. Show the weather info on your web server in the "/weather" route
#  2. If the weather degree below 10 show frozen emoji
#  3. If the weather degree above 30 show heat emoji
#  4. Anything else you can come up with. Be creative! :)
#  5. Run your Flask API with the command `flask --app 06_weather_app.py run --host=0.0.0.0`
