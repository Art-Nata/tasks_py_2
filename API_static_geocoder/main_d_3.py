import requests


def find_latitude(city):
    apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
    geocoder_req = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={city}&format=json"

    response = requests.get(geocoder_req)
    json_response = response.json()
    topon = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coord = topon["Point"]["pos"]
    long, latt = toponym_coord.split()
    return latt


list_city = input().split(',')

dict_city = {}

for c in list_city:
    dict_city[c] = find_latitude(c)
list_city_sorted = sorted(dict_city.items(), key=lambda x: x[1])
dict_city_sorted = dict(list_city_sorted)

print(list(dict_city_sorted.keys())[0])

