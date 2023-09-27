# TODO Mentors: Explain how do we get the specific information that we need from an API?

import requests

'''
Reads:
    What is json? https://www.w3schools.com/whatis/whatis_json.asp
    Tips for the exercise: https://stackoverflow.com/questions/59067671/is-there-a-way-to-easily-handle-json-tree-data-in-python
'''

api_key="" # add your api key here
city="Amsterdam"
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}]&aqi=no'

response = requests.get(url)

# TODO TechWomen Exercise 1:  Get the weather degree for Amsterdam from the weather api for today

if response.status_code == 200:
    json_response = response.json()
    weather_today = {
        "city" : json_response["location"]["name"],
        "degree" : json_response["current"]["temp_c"]
    }
    print(weather_today)
else:
    print("There was a problem!")


# TODO TechWomen Exercise 2: Aren't you curious what's the weather in your home town? Let's find out.

# TODO TechWomen Exercise 3: Explore the JSON response from the Weather API and print out the weather condition as a text

if response.status_code == 200:
    json_response = response.json()
    weather_today = {
        "city" : json_response["location"]["name"],
        "degree" : json_response["current"]["condition"]["text"]
    }
    print(weather_today)
else:
    print("There was a problem!")




