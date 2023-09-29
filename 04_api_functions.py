# TODO Mentors: Mentors explain the sequence of the execution with the functions

"""
Reads:
    Check out the functions tutorial that we learned in the morning :) https://github.com/TechWomenTribe/introduction_to_python/blob/main/tutorial/02_Functions.ipynb
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
