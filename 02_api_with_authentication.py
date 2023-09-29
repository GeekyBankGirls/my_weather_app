##############################
#
# An API (Application Programming Interface) is a set of rules and protocols that allows
# different software applications to communicate with each other.
# It defines how different software components should interact and exchange data.
# APIs are commonly used to enable third-party developers to access the functionality of
# a software platform or service.
#
##############################

# TODO Mentors: Explain what is an API & authentication & query string parameters


import requests

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
