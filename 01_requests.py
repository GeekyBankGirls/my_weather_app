##############################
#
# A Python package is a way of organizing and structuring Python code.
# It allows you to break down a large programming task into smaller,
# more manageable subtasks or modules.
# Packages are structured using “dotted module names” and can contain submodules.
# They help facilitate modular programming and make it easier to find,
# install, and share software developed by the Python community.
#
##############################

# TODO Mentors: Explain what is a python package generally and specifically requests & properties

import requests

url = f'https://www.google.com'

response = requests.get(url)

print(response.content)

# TODO TechWomen Exercise 1 : Print the output of the response

# TODO TechWomen Exercise 2 : Make a request to another web page

# TODO TechWomen Exercise 3 : Explore requests library and discuss the other options in the library
