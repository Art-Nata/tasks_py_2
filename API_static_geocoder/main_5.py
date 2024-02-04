import os

import pygame
import requests


apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
city = 'Австралия'

geocoder_req = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={city}&format=json"

response = requests.get(geocoder_req)
json_response = response.json()

toponim = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

toponym_coord = toponim["Point"]["pos"]
long, latt = toponym_coord.split()
ll = f'{long},{latt}'

toponim_delta = toponim['boundedBy']['Envelope']
x1, y1 = list(map(float, toponim_delta['lowerCorner'].split()))
x2, y2 = list(map(float, toponim_delta['upperCorner'].split()))
delta_x = (max(x1, x2) - min(x1, x2)) / 2
delta_y = (max(y1, y2) - min(y1, y2)) / 2
spn = f"{delta_x},{delta_y}"

map_params = {
    "ll": ll,
    "spn": spn,
    "l": "map",
}

map_api_server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(map_api_server, params=map_params)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)



