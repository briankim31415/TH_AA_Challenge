import requests
import urllib.request
import json


url = urllib.request.urlopen('https://aa-flight.herokuapp.com/flights?date=2020-01-01&origin=DFW').read()
flight_json = json.loads(url)[0]

print(flight_json)