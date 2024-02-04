import sys

import requests

from param_map import read_toponym, param_ll_spn


def main():
    adress = ''
    try:
        adress = " ".join(sys.argv[1:])
    except:
        print('No data')
        exit(1)

    if not adress:
        print('No data')
        exit(1)
    toponym_adress = read_toponym(adress)

    ll, spn = param_ll_spn(toponym_adress)
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": ll,
        "kind": "district",
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    try:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
    except:
        print('Ошибка выполнения запроса')
        exit(2)

    toponim_district = toponym["metaDataProperty"]["GeocoderMetaData"]['Components'][-1]['name']
    print(toponim_district)


if __name__ == '__main__':
    main()
