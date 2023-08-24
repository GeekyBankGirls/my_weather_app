# TODO Mentors: Explain the requirements

from flask import Flask
import requests

app = Flask(__name__)

api_key=""
city="Amsterdam"
url = f'http://api.weather.com/key="{api_key}"+&city="{city}'

response = requests.get(url)

# TODO TechGirls:
#  1. Show the weather info on your web server in the "/weather" route
#  2. If the weather degree below 10 show frozen emoji
#  3. If the weather degree above 30 show heat emoji
#  4. Anything else you can come up with. Be creative! :)

@app.route("/")
def get_weather():
    if response.status_code == 200:
        weather_today = {
            "city" : response.content["city"],
            "degree" : response.content["degree"]
        }
        return weather_today
    else:
        return "There was a problem!"


