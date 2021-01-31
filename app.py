from flask import Flask, render_template, request, session
import sqlite3
from datetime import datetime
import requests
import urllib.request
import json

app = Flask(__name__)
app.config["DEBUG"] = True
conn = sqlite3.connect('rr.db')
c = conn.cursor()
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
try:
    c.execute('''CREATE TABLE rrline (passenger_id, passenger_name, time)''')
except:
    pass
conn.commit()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form['name']
        session['name'] = name
        flight_num = request.form['flight-number']
        session['flight-number'] = flight_num
        print(name, flight_num)
        return render_template('next_page.html')
    # return "Hello World"
    # url = urllib.request.urlopen('https://aa-flight.herokuapp.com/flights?date=2020-01-01&origin=DFW').read()
    # flight_json = json.loads(url)
    # return flight_json[0]['flightNumber']
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

