from flask import Flask, render_template, request, session
import sqlite3
from datetime import datetime
import requests
import urllib.request
import json
import folium

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
def index():
    if request.method == "POST":
        name = request.form['name']
        session['name'] = name
        flight_num = request.form['flight-number']
        session['flight-number'] = flight_num
        return render_template('home.html')
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
        print(flight['flightNumber'])
        if str(flight['flightNumber']) == ft_nb:
            depart = {'city':flight['origin']['city'],'latitude':flight['origin']['location']['latitude'],'longitude':flight['origin']['location']['longitude']}
            destin = {'city':flight['destination']['city'],'latitude':flight['destination']['location']['latitude'],'longitude':flight['destination']['location']['longitude']}
            total_flight = {'time':flight['duration']['locale'],'distance':flight['distance']}
            # session['dplat'] = float(depart['latitude'])
            # session['dplong'] = -float(depart['longitude'])
            # session['dslat'] = float(destin['latitude'])
            # session['dslong'] = -float(destin['longitude'])
            lat1 = float(depart['latitude'])
            long1 = -float(depart['longitude'])
            lat2 = float(destin['latitude'])
            long2 = -float(destin['longitude'])

            m = folium.Map(location=[(lat1+lat2)/2,(long1+long2)/2], zoom_start=5)
            folium.Marker(location=[lat1,long1]).add_to(m)
            folium.Marker(location=[lat2,long2]).add_to(m)
            m.save('map.html')

        # return render_template('index.html')
            return render_template('flight_data.html' , dpcity = depart['city'], dplat = depart['latitude'], dplong = depart['longitude'], \
                dscity = destin['city'], dslat = destin['latitude'], dslong = destin['longitude'], ft_time = total_flight['time'], distance = total_flight['distance'])

@app.route('/chat.html')
def chat():
    return render_template('chat.html')

@app.route('/flight_hub.html', methods = ['GET', 'POST'])
def hub():
    return render_template('flight_hub.html')

@app.route('/home.html', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')
        
@app.route('/store.html')
def store():
    return render_template('store.html')

@app.route('/flight_schedule.html')
def flight_sched():
    return render_template('flight_schedule.html')

@app.route('/flight_menu.html')
def flight_menu():
    return render_template('flight_menu.html')

@app.route('/bathroom.html', methods = ['GET', 'POST'])
def bathroom():
    return render_template('bathroom.html')


# @app.route('/')

if __name__ == "__main__":
    app.run(debug=True)