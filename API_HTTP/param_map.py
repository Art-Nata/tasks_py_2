import requests


def read_toponym(adress):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": adress,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
    else:
        print('Ошибка выполнения запроса')
        toponym = None

    return toponym


def param_ll_spn(topon):
    toponym_coord = topon["Point"]["pos"]
    long, latt = toponym_coord.split()
    ll1 = f'{long},{latt}'

    toponim_delta = topon['boundedBy']['Envelope']
    x1, y1 = list(map(float, toponim_delta['lowerCorner'].split()))
    x2, y2 = list(map(float, toponim_delta['upperCorner'].split()))
    delta_x = (max(x1, x2) - min(x1, x2)) / 2
    delta_y = (max(y1, y2) - min(y1, y2)) / 2
    spn1 = f"{delta_x},{delta_y}"

    return ll1, spn1