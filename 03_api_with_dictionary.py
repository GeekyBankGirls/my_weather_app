import requests

# TODO Mentors: Explain how do we get the specific information that we need from an API?

api_key=""
city="Amsterdam"
url = f'http://api.weather.com/key="{api_key}"+&city="{city}'

# TODO Organizers: will check the parameters from the api & adjust this page

response = requests.get(url)

# TODO TechGirls:  Get the weather degree for Amsterdam from the weather api for today

if response.status_code == 200:
    weather_today = {
        "city" : response.content["city"],
        "degree" : response.content["degree"]
    }
    print(weather_today)
else:
    print("There was a problem!")


# TODO TechGirls: Aren't you curious what's the weather in your home town? Let's check it out.




