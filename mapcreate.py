import folium
import requests
import urllib.request
import json
from datetime import datetime

ft_nb = 9372

date_str = str(datetime.now()).split(' ')[0]
url = urllib.request.urlopen('https://aa-flight.herokuapp.com/flights?date=' + date_str + '&origin=DFW').read()
flight_json = json.loads(url)
for flight in flight_json:
    if str(flight['flightNumber']) == ft_nb:
        depart = {'city':flight['origin']['city'],'latitude':flight['origin']['location']['latitude'],'longitude':flight['origin']['location']['longitude']}
        destin = {'city':flight['destination']['city'],'latitude':flight['destination']['location']['latitude'],'longitude':flight['destination']['location']['longitude']}
        total_flight = {'time':flight['duration']['locale'],'distance':flight['distance']}

        lat1 = float(depart['latitude'])
        long1 = -float(depart['longitude'])
        lat2 = float(destin['latitude'])
        long2 = -float(destin['longitude'])

        m = folium.Map(location=[(lat1+lat2)/2,(long1+long2)/2], zoom_start=5)
        folium.Marker(location=[lat1,long1]).add_to(m)
        folium.Marker(location=[lat2,long2]).add_to(m)
        m.save(os.path.join(save_path, 'map.html'))
