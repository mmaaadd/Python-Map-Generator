import folium
import pandas
from geopy.geocoders import ArcGIS

# Read favourite places addresses from CSV and convert into list
data = pandas.read_csv("places.csv",header=0)
list_data = data["location"]

# Activate goecoder
geolocator = ArcGIS().geocode

# create list of coordinates of favourite places
list_coordinates = []
for location in list_data:
    geolocalization = geolocator(location)
    list_coordinates.append([geolocalization.latitude, geolocalization.longitude])

# Initiate map
map = folium.Map(location=[list_coordinates[0][0], list_coordinates[0][1]], zoom_start=3)

# create feature group for fav places
fg1 = folium.FeatureGroup(name = "My Places")

# add fav places to feature group
for coordinate, name in zip(list_coordinates, list_data):
    iframe = folium.IFrame(html=name, width=200, height=100)
    # fg.add_child(folium.Marker(location=[coordinate[0], coordinate[1]], popup=folium.Popup(iframe), icon=folium.Icon(color='lightgray', icon='circle', prefix='fa')))
    folium.CircleMarker(location=(coordinate[0], coordinate[1]),radius=10, fill_color='red', color = 'grey', fill_opacity=0.8, popup=folium.Popup(iframe)).add_to(fg1)

# create feature group for world population layer
fg2 = folium.FeatureGroup(name = "World population")
# read data from JSON and add conditional format depending on population
folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if x['properties']['POP2005'] < 100000000 else 'red' }, name="geojson").add_to(fg2)

# add both feature groups to map
map.add_child(fg1)
map.add_child(fg2)

# add controler to turn layers ON and OFF
map.add_child(folium.LayerControl())

# generate a map
map.save("Map_html_popup_simple.html")



