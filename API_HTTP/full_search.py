import sys
from io import BytesIO

import requests
from PIL import Image

from API_HTTP.param_map import param_ll_spn

# Пусть наше приложение предполагает запуск:
# python file.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    # обработка ошибочной ситуации
    pass


json_response = response.json()

toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]

ll, spn = param_ll_spn(toponym)

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "ll": ll,
    "spn": spn,
    "l": "map",
    "pt": "{0},pm2dgl".format(ll)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
