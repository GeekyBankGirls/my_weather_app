# TODO Mentors: Explain the concept of a web server & routes

from flask import Flask
import requests

app = Flask(__name__)

api_key=""
city="Amsterdam"
url = f'http://api.weather.com/key="{api_key}"+&city="{city}'

response = requests.get(url)

@app.route("/")
def get_weather():
        data = response.json()
        return data

# TODO Exercise: add a page called 'about' which shows your name & your city

