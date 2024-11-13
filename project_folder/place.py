class Place:
    def __init__(self, data):
        self.longitude = data["longitude"]
        self.latitude = data["latitude"]
        self.name = data["name"]
        self.state = data["state"]