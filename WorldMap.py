import pandas
import folium


data=pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


map = folium.Map(location=[27.2038,77.5011],zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="WorldMap")

for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el)+"meters",parse_html=True), icon=folium.Icon(color='red')))
    
map.add_child(fg)

map.save("WorldMap.html")