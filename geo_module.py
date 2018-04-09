import requests


def get_ll_spn(j_toponym):
    envelope = j_toponym["boundedBy"]["Envelope"]
    low_lon,  low_lat = map(lambda x: float(x), envelope["lowerCorner"].split())
    up_lon, up_lat = map(lambda x: float(x), envelope["upperCorner"].split())
    spn = str(up_lon - low_lon) + "," + str(up_lat - low_lat)
    ll = ",".join(j_toponym["Point"]["pos"].split())
    return ll, spn


def geocode(toponym, annotation=False):
    try:
        geocoder_url = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "format": "json",
            "geocode": toponym
        }

        response = requests.get(geocoder_url, params=geocoder_params)
        toponym = response.json()["response"]["GeoObjectCollection"]["featureMember"]

        if toponym:
            ll, spn = get_ll_spn(toponym[0]["GeoObject"])
            params = {
                "ll": ll,
                "spn": spn,
                "l": "sat,skl"
            }
            if annotation:
                return params, toponym[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
            return params

    except Exception as err:
        print(err)


def static(params):
    try:

        static_url = "http://static-maps.yandex.ru/1.x/"
        return static_url + "?" + "&".join(map(lambda x: x + "=" + params[x], params))

    except Exception as err:
        print(err)
