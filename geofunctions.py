import requests


def get_geo_object_by_toponym(toponym, index=0):
    geo_server = "http://geocode-maps.yandex.ru/1.x/"
    geo_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym,
        "format": "json"
    }
    response = requests.get(geo_server, geo_params)
    if not response:
        return None
    object_collection = response.json()["response"]["GeoObjectCollection"]["featureMember"]
    if len(object_collection) <= index:
        return None
    return object_collection[index]["GeoObject"]


def get_pos_by_geo_object(geo_object):
    geo_object_pos = ','.join(geo_object["Point"]["pos"].split())
    return geo_object_pos


def get_spn_by_geo_object(geo_object):
    geo_object_pos = tuple(map(float, geo_object["Point"]["pos"].split()))
    geo_object_lower_corner = tuple(map(float, geo_object["boundedBy"]["Envelope"]["lowerCorner"].split()))
    spn = f"{geo_object_pos[0] - geo_object_lower_corner[0]},{geo_object_pos[1] - geo_object_lower_corner[1]}"
    return spn
