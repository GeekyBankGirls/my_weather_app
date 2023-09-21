# TODO Mentors: Explain what is a python package generally and specifically requests & properties

## TODO Organizers: Add a link as a reference

import requests

url = f'https://www.google.com'

response = requests.get(url)

# TODO TechGirls: Print the output of the response

print(response.content)