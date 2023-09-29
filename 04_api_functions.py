# TODO Mentors: Mentors explain the sequence of the execution with the functions

import requests

api_key=""
city="Amsterdam"
url = f'http://api.weather.com/key="{api_key}"+&city="{city}'

response = requests.get(url)

# TODO TechGirls:
#  1. Add everything in a function that returns the response or the message "There was a problem!"
#  2. Call the function
#  3. Print the result of the function


def get_weather():
    if response.status_code == 200:
        weather_today = {
            "city" : response.content["city"],
            "degree" : response.content["degree"]
        }
        return weather_today
    else:
        return "There was a problem!"


print(get_weather())
