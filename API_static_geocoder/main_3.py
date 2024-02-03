import requests


def find_region(city):
    apikey = "40d1649f-0493-4b70-98ba-98533de7710b"

    geocoder_req = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={city}&format=json"

    response = requests.get(geocoder_req)
    json_response = response.json()

    toponim = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponim_post = toponim["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
    return toponim_post


def main():
    adress = 'Москва, Петровка, 38'
    postal = find_region(adress)
    print(f'{adress} имеет индекс: {postal}')


if __name__ == '__main__':
    main()
