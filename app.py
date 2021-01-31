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
            m = folium.Map(location=[(float(depart['latitude'])+float(destin['latitude']))/2,(-float(depart['longitude'])+-float(destin['longitude']))/2], zoom_starts=7)
            folium.Marker(location=[float(depart['latitude']),-float(depart['longitude'])]).add_to(m)
            folium.Marker(location=[float(destin['latitude']),-float(destin['longitude'])]).add_to(m)
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
    

# @app.route('/')

if __name__ == "__main__":
    app.run(debug=True)