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
        return render_template('index.html')
    # url = urllib.request.urlopen('https://aa-flight.herokuapp.com/flights?date=2020-01-01&origin=DFW').read()
    # flight_json = json.loads(url)
    # return flight_json[0]['flightNumber']
    return render_template('index.html')

@app.route('/flight_data.html')
def data():
    date_str = str(datetime.now()).split(' ')[0]
    url = urllib.request.urlopen('https://aa-flight.herokuapp.com/flights?date=' + date_str + '&origin=DFW').read()
    flight_json = json.loads(url)
    ft_nb = str(session.get('flight-number'))
    for flight in flight_json:
        # print(flight['origin']['city'], ft_nb)
        print(flight['flightNumber'])
        if str(flight['flightNumber']) == ft_nb:
            depart = {'city':flight['origin']['city'],'latitude':flight['origin']['location']['latitude'],'longitude':flight['origin']['location']['longitude']}
            destin = {'city':flight['destination']['city'],'latitude':flight['destination']['location']['latitude'],'longitude':flight['destination']['location']['longitude']}
            total_flight = {'time':flight['duration']['locale'],'distance':flight['distance']}
        # return render_template('index.html')
            return render_template('flight_data.html' , dpcity = depart['city'], dplat = depart['latitude'], dplong = depart['longitude'], \
                dscity = destin['city'], dslat = destin['latitude'], dslong = destin['longitude'], ft_time = total_flight['time'], distance = total_flight['distance'])

if __name__ == "__main__":
    app.run(debug=True)