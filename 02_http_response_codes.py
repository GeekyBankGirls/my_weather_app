# TODO Mentors: Explain HTTP codes & statuses

import requests

url = f'http://www.google.com'

response = requests.get(url)

# TODO TechGirls Exercise 1: Get a HTTP response of 200 code and print it
print(response)

# TODO TechGirls Exercise 2: Get a HTTP response of 404 code and print it

url = f'http://www.google.com/mycoolwebsite'

response = requests.get(url)
print(response)

# TODO TechGirls Exercise 3: Add a condition that checks whether the HTTP status code is 200 and print the output

url = f'http://www.google.com'

response = requests.get(url)

if response.status_code == 200:
    print("All good in the hood!")