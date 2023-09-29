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

# TODO TechGirls: Print the output of the response

print(response.content)
