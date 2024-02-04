import os
import sys

import pygame
import requests

from param_map import read_toponym, param_ll_spn


def find_biz(ll, spn, biz):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

    search_params = {
        "apikey": api_key,
        "text": biz,
        "lang": "ru_RU",
        "ll": ll,
        "snp": spn,
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
    else:
        raise RuntimeError('Ошибка выполнения запроса')
    organizations = json_response["features"]
    if len(organizations):
        return organizations[0]

print(111)
list_adress = sys.argv[1:]
print(list_adress)
adress = " ".join(list_adress)
print(adress)
toponym_adress = read_toponym(adress)
print(toponym_adress)
ll, spn = param_ll_spn(toponym_adress)
print(ll, spn)

apteka = find_biz(ll, "0.005,0.005", 'аптека')
apteka_point = apteka["geometry"]["coordinates"]
apteka_ll = f"{apteka_point[0]},{apteka_point[1]}"
map_request = f"http://static-maps.yandex.ru/1.x/?l='map'&lang=ru_RU&pt={ll},pm2db~{apteka_ll},pm2gn"
response = requests.get(map_request)

map_file = "map.png"
try:
    with open(map_file, "wb") as file:
        file.write(response.content)
except IOError as ex:
    print("Ошибка записи временного файла:", ex)

pygame.init()
screen = pygame.display.set_mode((600, 500))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()
os.remove(map_file)
