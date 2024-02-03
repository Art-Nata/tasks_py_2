import requests

adress = "Москва, Красная площадь, 1"

apikey = "40d1649f-0493-4b70-98ba-98533de7710b"

geocoder_req = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={adress}&format=json"

response = requests.get(geocoder_req)
json_response = response.json()

toponim = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

toponim_coord = toponim["Point"]["pos"]
toponim_adress = toponim["metaDataProperty"]["GeocoderMetaData"]["text"]

print(f"{toponim_adress} имеет координаты: {toponim_coord}")
