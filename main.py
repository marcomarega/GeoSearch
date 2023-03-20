import sys

from PIL import Image
from io import BytesIO
from geofunctions import *

if __name__ == "__main__":
    toponym = " ".join(sys.argv[1:])
    geo_object = get_geo_object_by_toponym(toponym)
    if geo_object is None:
        print("Error: bad geocoder response")
        sys.exit(1)
    static_server = "https://static-maps.yandex.ru/1.x/"
    static_params = {
        "ll": get_pos_by_geo_object(geo_object),
        "spn": get_spn_by_geo_object(geo_object),
        "l": "sat"
    }
    response = requests.get(static_server, static_params)
    if not response:
        print("Error: bad static api response")
        sys.exit(1)
    Image.open(BytesIO(response.content)).show()
