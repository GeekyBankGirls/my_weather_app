from flask import Flask, render_template, request
import requests

# TODO: add explanation for api & mentor will explain

api_key=""
url = f'http://api.weather.com/key="{api_key}"'

response = requests.get(url)

#TODO: print the output of the repsonse of the api

