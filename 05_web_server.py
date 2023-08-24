from flask import Flask, render_template, request
import requests

# TODO: Mentors explain the sequence of the execution with the functions

api_key=""
url = f'http://api.weather.com/key="{api_key}"'

response = requests.get(url)

#TODO: add everything in a function


