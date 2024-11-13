import json
import urllib.request
from get_apod import AstroPhoto


def get_apods_between(api_key, start_date, end_date):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={start_date}&end_date={end_date}"

    with urllib.request.urlopen(url) as request:
        response = request.read().decode()

    photos = []
    for item in json.loads(response):
        photos.append(AstroPhoto(item))

    return photos