import phonenumbers
import opencage
import folium
from phoneNUMBERtracer import track_NUMBER
from phonenumbers import geocoder

pep_NUMBER = phonenumbers.parse(track_NUMBER)
location = geocoder.description_for_number(pep_NUMBER, "en")
print(location)
from phonenumbers import carrier
service_pro = phonenumbers.parse(track_NUMBER)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key = "df8f13397ef94bcf9cee8a1f730d5d18"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("myLocation.html")