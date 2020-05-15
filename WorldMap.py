import pandas
import folium


data=pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 2000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[27.2038,77.5011],
zoom_start=6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="volcanos")

for lt, ln, el in zip(lat,lon,elev):
    # fg.add_child(folium.Marker(location=[lt, ln],
    #  popup=folium.Popup(str(el)+ " meters",parse_html=True), 
    #  icon=folium.Icon(color=color_producer(el))))
    
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius=12,
     popup=folium.Popup(str(el)+ " meters",parse_html=True), fill_color=color_producer(el),
     color='lightblue',fill_opacity=0.6, fill=True)) 

fgp = folium.FeatureGroup(name="polygons")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# fg.add_child(folium.GeoJson(data=(open('world.json',encoding='utf-8-sig').read(),

# style_function= lambda x: {'fillColor:'green' if x ['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x ['properties']['POP2005'] < 20000000 else 'red'}

# )))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("WorldMap.html")
