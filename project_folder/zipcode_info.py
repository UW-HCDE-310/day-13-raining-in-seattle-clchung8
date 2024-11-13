import urllib.request
import json


class Place:
    def __init__(self, name, latitude, longitude, state):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.state = state

    def __repr__(self):
        return f"Place(name={self.name}, latitude={self.latitude}, longitude={self.longitude}, state={self.state})"


def zipcode_info(countrycode, zipcode):
    url = f"https://api.zippopotam.us/{countrycode}/{zipcode}"
    with urllib.request.urlopen(url) as request:
        data = json.load(request)

    places = data["places"]

    place_list = [
        Place(
            place["place name"],
            place["latitude"],
            place["longitude"],
            place["state"]
        )
        for place in places
    ]

    return place_list
