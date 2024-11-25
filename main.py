from opencage.geocoder import OpenCageGeocode
from Калькулятор import resalt


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]["geometry"]["lat"], results[0]["geometry"]["lat"]
    else:
        return "Город не найден"


key = '1d18c2b84a624882bca2ab730b049a0e'
city = "Moscow"
coordinates = get_coordinates(city, key)

print(f"Координаты города {city} : {coordinates}")


