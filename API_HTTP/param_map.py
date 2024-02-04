import requests


def param_ll_spn(topon):
    toponym_coord = topon["Point"]["pos"]
    long, latt = toponym_coord.split()
    ll1 = f'{long},{latt}'

    toponim_delta = topon['boundedBy']['Envelope']
    x1, y1 = list(map(float, toponim_delta['lowerCorner'].split()))
    x2, y2 = list(map(float, toponim_delta['upperCorner'].split()))
    delta_x = (max(x1, x2) - min(x1, x2))
    delta_y = (max(y1, y2) - min(y1, y2))
    spn1 = f"{delta_x},{delta_y}"

    return ll1, spn1