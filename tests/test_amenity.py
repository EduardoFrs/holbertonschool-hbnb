import unittest
from pydantic import ValidationError
from ..Model.amenities import Amenity


class TestAmenity(unittest.TestCase):

    def test_valid_amenity(self):
        amenity = Amenity(name="Wi-Fi")
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "Wi-Fi")

    def test_missing_name(self):
        with self.assertRaises(ValidationError) as cm:
            Amenity()
        self.assertEqual(str(cm.exception), '"name" is required')


if __name__ == "__main__":
    unittest.main()
