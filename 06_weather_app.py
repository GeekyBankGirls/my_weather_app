# TODO Mentors: Explain the requirements of the exercise

from flask import Flask
import requests

app = Flask(__name__)

api_key="" # add your api key here
city="Amsterdam"
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}]&aqi=no'

response = requests.get(url)

# TODO TechWomen Last Exercise 1:
#  1. Show the weather info on your web server in the "/weather" route
#  2. If the weather degree below 10 show frozen emoji
#  3. If the weather degree above 30 show heat emoji
#  4. Anything else you can come up with. Be creative! :)
#  5. Run your Flask API with the command `flask --app 06_weather_app.py run --host=0.0.0.0`
