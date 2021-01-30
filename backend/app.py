from flask import Flask
import requests
import urllib.request
import json

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])

def home():
    # return "Hello World"
    url = urllib.request.urlopen('https://aa-flight.herokuapp.com/flights?date=2020-01-01&origin=DFW').read()
    flight_json = json.loads(url)
    return flight_json[0]['flightNumber']

if __name__ == "__main__":
    app.run(debug=True)