import json
import urllib.request


class AstroPhoto:
    def __init__(self, data):
        self.title = data["title"]
        self.date = data["date"]
        self.description = data["explanation"]
        self.url = data["hdurl"]

    def get_short_description(self):
        if len(self.description) <= 200:
            return self.description
        else:
            return self.description[:197] + "..."


def get_apod(api_key, date=None):
    if date:
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    else:
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    with urllib.request.urlopen(url) as request:
        response = request.read().decode()

    return AstroPhoto(json.loads(response))