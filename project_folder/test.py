import unittest
from project_folder.get_apod_between import get_apods_between
from project_folder.zipcode_info import zipcode_info
from project_folder.get_apod import AstroPhoto, get_apod
from project_folder.place import Place


class TestAPIFunctions(unittest.TestCase):

    def test_get_apod(self):
        api_key = "DEMO_KEY"
        apod = get_apod(api_key, "2022-12-31")

        self.assertIsInstance(apod, AstroPhoto)
        self.assertEqual(apod.title, "Moon over Makemake")

    def test_get_apods_between(self):
        api_key = "DEMO_KEY"
        apods = get_apods_between(api_key, "2022-01-01", "2022-01-07")

        self.assertIsInstance(apods, list)
        self.assertGreater(len(apods), 0)

    def test_zipcode_info(self):
        info = zipcode_info("US", "98105")

        self.assertIsInstance(info, list)
        self.assertGreater(len(info), 0)

        info_multiple = zipcode_info("US", "02861")
        self.assertGreater(len(info_multiple), 1)

    def test_place_class(self):
        mock_data = {
            "longitude": "-122.3022",
            "latitude": "47.6633",
            "name": "Seattle",
            "state": "Washington"
        }
        place = Place(mock_data)

        self.assertEqual(place.name, "Seattle")
        self.assertEqual(place.state, "Washington")
        self.assertEqual(place.longitude, "-122.3022")
        self.assertEqual(place.latitude, "47.6633")


if __name__ == '__main__':
    unittest.main()
