from django.templatetags.i18n import language
from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]["geometry"]["lat"], 2)
            lon = round(results[0]["geometry"]["lng"], 2)
            return lat, lon
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка {e}"


key = '1d18c2b84a624882bca2ab730b049a0e'
city = "Makhachkala"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city} : {coordinates}")


