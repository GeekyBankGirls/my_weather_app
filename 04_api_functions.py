# TODO Mentors: Mentors explain the sequence of the execution with the functions

"""
Reads:
    Check out the functions class that we learned in the morning :) https://github.com/TechWomenTribe/introduction_to_python/blob/main/tutorial/02_Functions.ipynb
"""

import requests

api_key="" # add your api key here
city="Amsterdam"
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}]&aqi=no'

response = requests.get(url)

# TODO TechWomen Exercise 1:
#  1. Add everything in a function that returns the city name and the temp_c value or the message "There was a problem!"
#  2. Call the function
#  3. Print the result of the function


def get_weather():
    if response.status_code == 200:
        json_response = response.json()
        weather_today = {
            "city": json_response["location"]["name"],
            "degree": json_response["current"]["temp_c"]
        }
        print(weather_today)
    else:
        print("There was a problem!")


print(get_weather())


