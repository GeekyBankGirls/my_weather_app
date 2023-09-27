# TODO Mentors: Explain what is a python package generally and specifically requests & properties

"""
Reads:
    What is a Python package? https://www.geeksforgeeks.org/python-packages/
    What is HTTP? What is Python Requests Library? https://www.dataquest.io/blog/tutorial-an-introduction-to-python-requests-library/
"""

import requests

url = f'https://www.google.com'

response = requests.get(url)

print(response.content)

# TODO TechWomen Exercise 1 : Print the output of the response

# TODO TechWomen Exercise 2 : Make a request to another web page

# TODO TechWomen Exercise 3 : Explore requests library and discuss the other options in the library