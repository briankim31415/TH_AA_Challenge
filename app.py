from flask import Flask, render_template, request, session
import sqlite3
from datetime import datetime
import requests
import urllib.request
import json
import folium
import os.path
import random
# from restroom import add_to_list, remove_from_list, query

save_path = './templates'

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

def add_to_list(passenger):
    passenger = passenger.replace(' ','_')
    ran = random.randint(5321,12359)
    curr_time = str(datetime.now())[11:16]
    c.execute('INSERT INTO rrline values(?,?,?)',(ran, passenger, curr_time))
    conn.commit()
    print('INSERT INTO rrline values(?,?,?)',(ran, passenger, curr_time))

def remove_from_list(id):
    id = str(id)
    c.execute('DELETE FROM rrline where passenger_id=(?)',[id])
    conn.commit()

def query():
    c.execute('SELECT length(time) FROM rrline')
    print(c.fetchall())
    return((int(str(c.fetchone()).split(',')[0].lstrip('('))))



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form['name']
        session['name'] = name
        flight_num = request.form['flight-number']
        session['flight-number'] = flight_num
        date_str = str(datetime.now()).split(' ')[0]
        url = urllib.request.urlopen('https://aa-flight.herokuapp.com/flights?date=' + date_str + '&origin=DFW').read()
        flight_json = json.loads(url)
        ft_nb = str(session.get('flight-number'))
        for flight in flight_json:
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
                m.save(os.path.join(save_path, 'map.html'))

        return render_template('home.html')
    # return render_template('home.html')
    return render_template('index.html')

@app.route('/chat.html')
def chat():
    return render_template('chat.html')

@app.route('/flight_hub.html', methods = ['GET', 'POST'])
def hub():
    return render_template('flight_hub.html')

@app.route('/home.html', methods = ['GET', 'POST'])
def home():
    print(session.get('name'))
    return render_template('home.html' , name = session.get('name'))
        
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
    if request.method == "GET":
        num_line = query()
        if num_line > 0:
            return render_template('bathroom_not_available.html' , num_line = num_line )
        else:
            return render_template ('bathroom_available.html')
    return render_template('bathroom.html')

@app.route('/bathroom_not_available.html', methods = ['POST'])
def join_line():
    if request.method == "GET":
        add_to_list(session.get('name'))
        return render_template ('home.html')
@app.route('/map.html')
def map():
    return render_template('map.html')


# @app.route('/')

if __name__ == "__main__":
    app.run(debug=True)
    c.close()
