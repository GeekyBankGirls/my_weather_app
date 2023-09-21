import requests

# TODO Mentors: Explain what is an API & authentication & query string parameters
# TODO Organizers: Add a link as a reference

api_key=""
url = f'http://api.weather.com/key="{api_key}"'

response = requests.get(url)

# TODO TechGirls:
#  Print the output of the response from the weather api if the status is 200
#  Print the output with an error message using else statement

if response.status_code == 200:
    print(response.content)
else:
    print("There was a problem!")




