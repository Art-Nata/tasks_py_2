import requests


def find_region(city):
    apikey = "40d1649f-0493-4b70-98ba-98533de7710b"

    geocoder_req = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={city}&format=json"

    response = requests.get(geocoder_req)
    json_response = response.json()

    toponim = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponim_adress = toponim["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"]
    return toponim_adress


for city in ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']:
    region = find_region(city)
    print(f'{city}: {region}')
