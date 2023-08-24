from flask import Flask, render_template, request
import requests

# TODO: add explanation for api & mentor will explain

api_key=""
url = f'http://api.weather.com'

response = requests.get(url)

# print the output of the url
