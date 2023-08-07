
# Geolocation

from geopy.distance import geodesic
from geopy.geocoders import Nominatim


newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(geodesic(newport_ri, cleveland_oh).miles)

geolocator = Nominatim(user_agent="Oleg")
location = geolocator.geocode("21 Symyrenka Kyiv")
print(location.address)
