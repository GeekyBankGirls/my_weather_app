##############################
#
# HTTP codes or HTTP status codes are standardized three-digit numbers that indicate the outcome of an HTTP request.
# They are issued by a server in response to a client’s request and provide information about the status of the request.
# HTTP status codes are grouped into five classes:
#
# Informational responses (100 – 199):
# These responses indicate that the request has been received and the server is continuing the process.

# Successful responses (200 – 299):
# These responses indicate that the request has been successfully completed.

# Redirection messages (300 – 399):
# These responses indicate that further action needs to be taken to complete the request.
#
# Client error responses (400 – 499):
# These responses indicate that there was an error on the client’s side, such as a malformed request or unauthorized access.
#
# Server error responses (500 – 599):
# These responses indicate that there was an error on the server’s side, such as an internal server error or a service being temporarily unavailable.
#
# For a comprehensive list of HTTP status codes and their explanations,
# you can refer to the Mozilla Developer Network (MDN) or SiteGround KB.
#
##############################

# TODO Mentors: Explain HTTP codes & statuses

"""
Reads:
    What are the HTTP codes? https://http.dev/status
"""

import requests

url = f'http://www.google.com'

response = requests.get(url)

# TODO TechWomen Exercise 1: Get a HTTP response of 200 code from the request and print the output

# TODO TechWomen Exercise 2: Get a HTTP response of 404 code from the request and print the output

# TODO TechWomen Exercise 3: Add a condition that checks whether the HTTP status code is 200 and print the output
